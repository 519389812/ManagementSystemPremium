from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.conf import settings
from django.core.paginator import Paginator
from performance.models import Position, WorkloadRecord, RewardRecord
from team.models import CustomTeam
from user.views import check_authority, check_grouping
from ManagementSystemPremium.views import parse_url_param
from django.utils import timezone
import pandas as pd
import numpy as np
import datetime
from django.contrib import messages
from io import BytesIO
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator

from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader('{}/templates/pyecharts'.format(settings.BASE_DIR)))

from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Grid, Page
from pyecharts.globals import ThemeType


def make_date_list(start_date, end_date):
    date_list = []
    day_delta = (end_date - start_date).days + 1
    for days in range(day_delta):
        the_date = (start_date + datetime.timedelta(days=days)).strftime('%Y-%m-%d')
        date_list.append(the_date)
    return date_list


def get_queryset(url_params, model_name):
    if len(url_params) > 0:
        filter_str = ''
        for key, value in url_params.items():
            if 'date' in key:
                filter_str += key.replace('__range', '') + '=' + value[0].replace('/', '-') + ', '
            elif 'id' in key:
                filter_str += key + '=' + value[0] + ', '
            else:
                filter_str += key + '=' + value[0] + ', '
        command_str = '%s.objects.filter(%s)' % (model_name, filter_str)
        queryset = eval(command_str)
    else:
        queryset = eval('%s.objects.all()' % model_name)
    return queryset


@check_authority
def reward_charts(request):
    url = request.META.get('HTTP_REFERER', '')
    if url == '':
        return render(request, 'error_400.html', status=400)
    url_params = parse_url_param(url)
    queryset = get_queryset(url_params, 'RewardRecord')
    if queryset.count() == 0:
        messages.error(request, '无数据')
        return redirect(url)

    # summary_line
    date_range = list(queryset.values_list('date', flat=True).order_by('date'))
    start_date, end_date = date_range[0], date_range[-1]
    date_list = make_date_list(start_date, end_date)
    data = pd.DataFrame(date_list, columns=['日期'])
    data_db = pd.DataFrame(queryset.values('user__last_name', 'user__first_name', 'reward__name', 'date'))
    data_db['name'] = data_db['user__last_name'] + data_db['user__first_name']
    data_db = data_db[['name', 'reward__name', 'date']]
    data_db = data_db.rename(columns={'name': '姓名', 'reward__name': '奖惩名称', 'date': '日期'})
    data_db['日期'] = data_db['日期'].apply(lambda x: x.strftime('%Y-%m-%d'))
    data = pd.merge(data, data_db, on='日期', how='left')
    data['次数'] = data['奖惩名称']
    data = pd.pivot_table(data, values=['次数'], index=['日期'], columns=['奖惩名称'], aggfunc=np.count_nonzero)
    data = data.fillna(0)
    _, second_list = zip(*data.columns.tolist())
    second_list = set(second_list)
    line = Line(init_opts=opts.InitOpts()).set_global_opts(title_opts=opts.TitleOpts(title='奖惩趋势', subtitle='总体'))
    line.add_xaxis(data.index.values.tolist())
    for value in second_list:
        line.add_yaxis(value, data['次数'][value], symbol_size=10, is_smooth=True)
    reward_summary_line = (
        line
    )

    # summary_bar
    data = pd.DataFrame(queryset.values('user__last_name', 'user__first_name', 'reward__name'))
    data['name'] = data['user__last_name'] + data['user__first_name']
    data = data[['name', 'reward__name']]
    data = data.rename(columns={'name': '姓名', 'reward__name': '奖惩名称'})
    data['次数'] = data['姓名']
    data = pd.pivot_table(data, values=['次数'], index=['奖惩名称'], aggfunc=np.count_nonzero)
    bar = Bar(init_opts=opts.InitOpts()).set_global_opts(title_opts=opts.TitleOpts(title='奖惩统计', subtitle='总体'))
    bar.add_xaxis(data.index.values.tolist())
    bar.add_yaxis('奖惩名称', data['次数'].values.tolist())
    reward_summary_bar = (
        bar
    )

    # summary_bar
    data = pd.DataFrame(queryset.values('user__last_name', 'user__first_name', 'reward__name'))
    data['name'] = data['user__last_name'] + data['user__first_name']
    data = data[['name', 'reward__name']]
    data = data.rename(columns={'name': '姓名', 'reward__name': '奖惩名称'})
    data['次数'] = data['姓名']
    data = pd.pivot_table(data, values=['次数'], index=['姓名', '奖惩名称'], aggfunc=np.count_nonzero)
    first_list, second_list = zip(*data.index.values)
    first_list = set(first_list)
    bar = Bar(init_opts=opts.InitOpts()).set_global_opts(title_opts=opts.TitleOpts(title='奖惩统计', subtitle='按姓名'))
    bar.add_xaxis(second_list)
    for value in first_list:
        bar.add_yaxis(value, data.loc[value]['次数'].values.tolist())
    reward_summary_by_name_bar = (
        bar
    )

    page = Page(layout=Page.SimplePageLayout, page_title='奖惩统计')
    page.add(reward_summary_line)
    page.add(reward_summary_bar)
    page.add(reward_summary_by_name_bar)
    return HttpResponse(page.render_embed())


@check_authority
def workload_summary_export(request):
    url = request.META.get('HTTP_REFERER', '')
    if url == '':
        return render(request, 'error_400.html', status=400)
    url_params = parse_url_param(url)
    queryset = get_queryset(url_params, 'WorkloadRecord')
    queryset = queryset.filter(verified=True)
    if queryset.count() == 0:
        messages.error(request, '无数据')
        return redirect(url)
    outfile = BytesIO()
    data = pd.DataFrame(queryset.values('user__last_name', 'user__first_name', 'score', 'workload', 'bonus', 'man_hours'))
    data['name'] = data['user__last_name'] + data['user__first_name']
    data = data.rename(columns={'name': '姓名', 'score': '分数', 'workload': '工作量', 'bonus': '奖金',
                                'man_hours': '工时'})
    data = data[['姓名', '分数', '工作量', '奖金', '工时']]
    data = data.sort_values(by=['姓名'], ascending=True)
    data = data.fillna('')
    data = pd.pivot_table(data, values=['分数', '工作量', '奖金', '工时'], index=['姓名'], aggfunc=np.sum)
    filename = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = "attachment;filename='{}'".format('Export pivot by score ' + filename + '.xlsx')
    data.to_excel(outfile)
    response.write(outfile.getvalue())
    return response


def performance(request):
    return render(request, 'performance.html')


def return_formfield_for_foreignkey(request, db_field, kwargs, db_field_name, obj):
    if not request.user.is_superuser:
        try:
            team_id = request.user.team.id
            if db_field.name == db_field_name:
                kwargs['queryset'] = obj.objects.filter(related_parent__iregex=r'\D%s\D' % str(team_id))
        except:
            pass
    return kwargs


@check_authority
@check_grouping
def add_workload(request):
    if request.user.team.parent:
        team_id = request.user.team.parent.id
    else:
        team_id = request.user.team.id
    team = request.user.team
    if not request.user.is_superuser:
        position_list = list(Position.objects.filter(team__in=[team]).order_by('name').values('id', 'name'))
        team_list = list(CustomTeam.objects.filter(related_parent__iregex=r'[^0-9]*%s[^0-9]' % str(team_id)).order_by('name'))
    else:
        position_list = list(Position.objects.all().order_by('name').values('id', 'name'))
        team_list = list(CustomTeam.objects.all().order_by('name'))
    team_list = [{'id': team.id, 'name': team.get_related_parent_name()} for team in team_list]
    if request.method == 'POST':
        date = request.POST.get('date', '')
        position_id = request.POST.get('position_id', '')
        number_people = request.POST.get('number_people', '')
        number_baggage = request.POST.get('number_baggage', '')
        sale = request.POST.get('sale', '')
        verifier_team_id = request.POST.get('verifier_team_id', '')
        remark = request.POST.get('remark', '')
        if not all([date, position_id, number_people, number_baggage, sale, verifier_team_id]):
            return render(request, 'error_500.html', status=500)
        try:
            position = Position.objects.get(id=int(position_id))
            verifier = CustomTeam.objects.get(id=int(verifier_team_id))
            WorkloadRecord.objects.create(user=request.user, date=date, position=position,
                                          number_people=int(number_people), number_baggage=int(number_baggage),
                                          sale=float(sale), verifier=verifier, remark=remark)
            msg = '登记成功！您可以继续登记下一条记录！'
            return render(request, 'add_workload.html',
                          {'position_list': position_list, 'team_list': team_list, 'position_name': position.name,
                           'verifier_team_name': verifier.name, 'msg': msg})
        except:
            return render(request, 'error_500.html', status=500)
    else:
        return render(request, 'add_workload.html', {'position_list': position_list, 'team_list': team_list})


@check_authority
def view_workload(request):
    if request.method == 'GET':
        page_num = request.GET.get('page', '1')
        create_datetime = timezone.localtime(timezone.now()) - timezone.timedelta(days=30)
        workload_list = WorkloadRecord.objects.filter(user=request.user, created_datetime__gte=create_datetime)
        paginator = Paginator(workload_list, 20)
        page = paginator.get_page(int(page_num))
        return render(request, 'view_workload.html', {'page_workload_list': list(page.object_list),
                                                      'total_workload': paginator.count,
                                                      'total_page_num': paginator.num_pages,
                                                      'page_num': page.number})
    else:
        return render(request, 'error_500.html', status=500)
