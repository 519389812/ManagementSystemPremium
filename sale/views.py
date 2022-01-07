from django.shortcuts import render
from user.views import check_authority, check_grouping
from sale.models import Product, SalesRecord
from user.models import CustomUser
from ManagementSystemPremium.views import *
from django.utils import timezone
from django.core.paginator import Paginator


def sales(request):
    return render(request, 'sales.html')


@check_authority
@check_grouping
def add_sales(request):
    product_list = list(Product.objects.all().order_by('name').values('id', 'name'))
    user_list = list(CustomUser.objects.all().order_by('full_name').values('id', 'full_name'))
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
        issue_user_id = request.POST.get('issue_user_id', '')
        if not all(
                [date, product_id, flight_number, passenger, ticket, emd, destination, amount, miles, issue_user_id]):
            return render(request, 'error_500.html', status=500)
        if not check_post_validate(request, check_date_validate, check_flight_validate, check_fullname_validate,
                                   check_ticket_validate, check_ticket_validate, check_airport_code_validate,
                                   check_amount_validate, check_amount_validate,
                                   ['date', 'flight_number', 'passenger', 'ticket', 'emd', 'destination', 'amount',
                                    'miles']):
            return render(request, 'add_sales.html', {'msg': '存在未按规定要求填写的字段！'})
        try:
            product = Product.objects.get(id=int(product_id))
            issue_user = CustomUser.objects.get(id=int(issue_user_id))
            SalesRecord.objects.create(date=date, product=product, flight_number=flight_number, passenger=passenger,
                                       ticket=ticket, emd=emd, destination=destination, issue_user=issue_user,
                                       amount=amount, miles=miles, user=request.user)
            return render(request, 'add_workload.html', {'user_list': user_list, 'product_list': product_list,
                                                         'msg': '登记成功！'})
        except:
            return render(request, 'error_500.html', status=500)
    else:
        return render(request, 'add_sales.html', {'user_list': user_list, 'product_list': product_list})


@check_authority
def view_sales(request):
    if request.method == 'GET':
        page_num = request.GET.get('page', '1')
        create_datetime = timezone.localtime(timezone.now()) - timezone.timedelta(days=30)
        sales_list = SalesRecord.objects.filter(user=request.user, create_datetime__gte=create_datetime)
        paginator = Paginator(sales_list, 30)
        page = paginator.get_page(int(page_num))
        return render(request, 'view_sales.html', {'page_sales_list': list(page.object_list),
                                                   'total_sales': paginator.count,
                                                   'total_page_num': paginator.num_pages,
                                                   'page_num': page.number})
    else:
        return render(request, 'error_500.html', status=500)
