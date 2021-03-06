import numpy as np
import pandas as pd
from django.shortcuts import render
from flexible.models import LoadSheet, LoadSheetContent, LoadSheetRecord
from django.core.paginator import Paginator


def view_loadsheet_list(request):
    if request.method == 'GET':
        page_num = request.GET.get('page', '1')
        load_sheet_list = LoadSheet.objects.all()
        load_sheet_list = list(load_sheet_list.values('id', 'flight', 'date'))
        paginator = Paginator(load_sheet_list, 30)
        page = paginator.get_page(int(page_num))
        return render(request, 'view_loadsheet_list.html', {'page_object_list': list(page.object_list),
                                                            'total_num': paginator.count,
                                                            'total_page_num': paginator.num_pages,
                                                            'page_num': page.number})
    else:
        return render(request, 'error_400.html', status=400)


def view_loadsheet(request):
    if request.method == 'GET':
        id_ = request.GET.get('id', '')
        try:
            load_sheet = LoadSheet.objects.get(id=id_)
        except:
            return render(request, 'error_404.html', status=404)
        return render(request, 'loadsheet.html', context={'load_sheet': load_sheet})


def add_loadsheet(request):
    if request.method == 'POST':
        params = request.POST.dict()
        load_sheet_id = params['load_sheet_id']
        answer_time = int(params['answer_time'])
        try:
            load_sheet = LoadSheet.objects.get(id=load_sheet_id)
        except:
            return render(request, 'error_500.html', status=500)
        if request.user.is_authenticated:
            user = request.user
            anonymous = ''
            times = LoadSheetRecord.objects.filter(load_sheet=load_sheet, user=request.user).count() + 1
        else:
            user = None
            anonymous = params['username']
            del (params['username'])
            times = LoadSheetRecord.objects.filter(load_sheet=load_sheet, anonymous=anonymous).count() + 1
        del(params['csrfmiddlewaretoken'])
        del(params['load_sheet_id'])
        del(params['answer_time'])
        data = {}
        data.setdefault('??????', {})
        data.setdefault('??????', {})
        data.setdefault('??????', {})
        for param_name, param_value in params.items():
            type_, id_, name = param_name.split('_')
            if name == 'destination' or name == 'location' or name == 'baggageLocation':
                param_value = param_value.upper()
            if type_ == 'fixPax':
                data['??????'].setdefault(id_, {})
                data['??????'][id_][name] = param_value
            elif type_ == 'fixBaggage':
                data['??????'].setdefault(id_, {})
                data['??????'][id_][name] = param_value
            elif type_ == 'fixOther':
                data['??????'].setdefault(id_, {})
                data['??????'][id_][name] = param_value
        load_sheet_content = LoadSheetContent.objects.filter(load_sheet__id=load_sheet_id)
        total_score = 0
        lcm_total = load_sheet.passenger
        weight_fixed = 0
        passenger_correct = False
        baggage_correct = False
        other_correct = False
        passenger, baggage, other = [pd.DataFrame(None)] * 3
        for key, value in data.items():
            df = pd.DataFrame(value).T
            if key == '??????':
                load_sheet_passenger = load_sheet_content.filter(project='??????').values('destination', '_class', 'type', 'number', 'weight')
                load_sheet_passenger = pd.DataFrame(load_sheet_passenger)
                if load_sheet_passenger.shape[0] > 0:
                    load_sheet_passenger.fillna('', inplace=True)
                    load_sheet_passenger = load_sheet_passenger.pivot_table(values=['number', 'weight'],
                                                                            index=['destination', '_class', 'type'],
                                                                            dropna=False, margins=True, margins_name='??????',
                                                                            aggfunc=np.sum)
                    load_sheet_passenger.dropna(inplace=True)
                if df.shape[0] > 0:
                    df['paxNumber'] = df['paxNumber'].apply(int)
                    df['paxWeight'] = df['paxWeight'].apply(int)
                    df = df.pivot_table(values=['paxNumber', 'paxWeight'], index=['destination', 'paxClass', 'paxType'], dropna=False, margins=True, margins_name='??????', aggfunc=np.sum)
                    df.dropna(inplace=True)
                    lcm_total += df.loc['??????', '', '']['paxNumber']
                    weight_fixed += df.loc['??????', '', '']['paxWeight']
                    passenger = df
                    if load_sheet_passenger.shape[0] == df.shape[0]:
                        if df.loc['??????', '', '']['paxNumber'] == load_sheet_passenger.loc['??????', '', '']['number'] and df.loc['??????', '', '']['paxWeight'] == load_sheet_passenger.loc['??????', '', '']['weight']:
                            correct = True
                        else:
                            correct = False
                    else:
                        correct = False

                else:
                    correct = True if load_sheet_passenger.shape[0] == 0 else False
                if correct:
                    total_score += 33.33
                    passenger_correct = True
            elif key == '??????':
                load_sheet_baggage = load_sheet_content.filter(project='??????').values('destination', 'location', 'number', 'weight')
                load_sheet_baggage = pd.DataFrame(load_sheet_baggage)
                if load_sheet_baggage.shape[0] > 0:
                    load_sheet_baggage.fillna('', inplace=True)
                    load_sheet_baggage = load_sheet_baggage.pivot_table(values=['number', 'weight'], index=['destination', 'location'], dropna=False, margins=True, margins_name='??????', aggfunc=np.sum)
                    load_sheet_baggage.dropna(inplace=True)
                if df.shape[0] > 0:
                    df['baggageNumber'] = df['baggageNumber'].apply(int)
                    df['baggageWeight'] = df['baggageWeight'].apply(int)
                    df = df.pivot_table(values=['baggageNumber', 'baggageWeight'], index=['destination', 'baggageLocation'], dropna=False, margins=True, margins_name='??????', aggfunc=np.sum)
                    df.dropna(inplace=True)
                    weight_fixed += df.loc['??????', '']['baggageWeight']
                    baggage = df
                    if load_sheet_baggage.shape[0] == df.shape[0]:
                        if df.loc['??????', '']['baggageNumber'] == load_sheet_baggage.loc['??????', '']['number'] and df.loc['??????', '']['baggageWeight'] == load_sheet_baggage.loc['??????', '']['weight']:
                            correct = True
                        else:
                            correct = False
                    else:
                        correct = False
                else:
                    correct = True if load_sheet_baggage.shape[0] == 0 else False
                if correct:
                    total_score += 33.33
                    baggage_correct = True
            elif key == '??????':
                load_sheet_other = load_sheet_content.filter(project='??????').values('destination', 'location', 'type', 'weight')
                load_sheet_other = pd.DataFrame(load_sheet_other)
                if load_sheet_other.shape[0] > 0:
                    load_sheet_other.fillna('', inplace=True)
                    load_sheet_other = load_sheet_other.pivot_table(values=['weight'],
                                                                    index=['destination', 'location', 'type'], dropna=False,
                                                                    margins=True, margins_name='??????', aggfunc=np.sum)
                    load_sheet_other.dropna(inplace=True)
                if df.shape[0] > 0:
                    df['weight'] = df['weight'].apply(int)
                    df = df.pivot_table(values=['weight'], index=['destination', 'location', 'type'], dropna=False, margins=True, margins_name='??????', aggfunc=np.sum)
                    df.dropna(inplace=True)
                    weight_fixed += df.loc['??????', '', '']['weight']
                    other = df
                    if load_sheet_other.shape[0] == df.shape[0]:
                        if df.loc['??????', '', '']['weight'] == load_sheet_other.loc['??????', '', '']['weight']:
                            correct = True
                        else:
                            correct = False
                    else:
                        correct = False
                else:
                    correct = True if load_sheet_other.shape[0] == 0 else False
                if correct:
                    total_score += 33.33
                    other_correct = True
        total_score = round(total_score, 0)
        LoadSheetRecord.objects.create(user=user, anonymous=anonymous, load_sheet=load_sheet, answer_time=answer_time,
                                       times=times, score=total_score)
        return render(request, 'view_loadsheet.html', {'total_score': total_score, 'lcm_total': lcm_total,
                                                       'weight_fixed': weight_fixed, 'passenger': passenger,
                                                       'baggage': baggage, 'other': other,
                                                       'passenger_correct': passenger_correct,
                                                       'baggage_correct': baggage_correct,
                                                       'other_correct': other_correct})
    else:
        return render(request, 'error_403.html', status=403)
