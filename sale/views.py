from django.shortcuts import render
from user.views import check_authority, check_grouping
from sale.models import Product
from user.models import CustomUser
from ManagementSystemPremium.views import *


def sales(request):
    return render(request, 'sales.html')


@check_authority
@check_grouping
def add_sales(request):
    user_list = list(CustomUser.objects.all().order_by('full_name').values('id', 'full_name'))
    product_list = list(Product.objects.all().order_by('name').values('id', 'name'))
    if request.method == 'POST':
        date = request.POST.get('date', '')
        product_id = request.POST.get('product_id', '')
        flight_number = request.POST.get('flight_number', '')
        passenger = request.POST.get('passenger', '')
        ticket = request.POST.get('ticket', '')
        emd = request.POST.get('emd', '')
        destination = request.POST.get('destination', '')
        amount = request.POST.get('amount', '')
        miles = request.POST.get('miles', '')
        issue_user = request.POST.get('issue_user_id', '')
        if not all([date, product_id, flight_number, passenger, ticket, emd, destination, amount, miles, issue_user]):
            return render(request, 'error_500.html', status=500)
        if not check_post_validate(request, check_date_validate, check_flight_validate, check_fullname_validate,
                                   check_ticket_validate, check_ticket_validate, check_airport_code_validate,
                                   check_amount_validate, check_amount_validate,
                                   ['date', 'flight_number', 'passenger', 'ticket', 'emd', 'destination', 'amount', 'miles']):
            return render(request, 'add_sales.html', {'msg': '存在未按规定要求填写的字段！'})
        try:
            post_dict = (dict(request.POST))
            post_dict = {k: int(v[0]) for k, v in post_dict.items() if k not in ['date', 'position_id', 'verifier_team_id', 'remark', 'csrfmiddlewaretoken']}
            position_workload_item_list = list(WorkloadItem.objects.filter(position__id=int(position_id)).values_list('name', flat=True))
            if set(list(post_dict.keys())) != set(position_workload_item_list):
                return render(request, 'error_500.html', status=500)
            post_dict = json.dumps(post_dict)
            position = Position.objects.get(id=int(position_id))
            verifier = CustomTeam.objects.get(id=int(verifier_team_id))
            WorkloadRecord.objects.create(user=request.user, date=date, position=position, workload=post_dict,
                                          verifier=verifier, remark=remark)
            msg = '登记成功！您可以继续登记下一条记录！'
            return render(request, 'add_workload.html', {'position_list': position_list, 'team_list': team_list, 'msg': msg})
        except:
            return render(request, 'error_500.html', status=500)
    else:
        return render(request, 'add_sales.html', {'user_list': user_list, 'product_list': product_list})
