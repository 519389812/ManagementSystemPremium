from django.shortcuts import render
from .models import Current, Rack, CurrentRecord, CurrentStorage
from user.views import check_is_superuser, check_authority


def asset(request):
    return render(request, 'asset.html')


@check_authority
def warehousing(request):
    in_out = request.GET.get('in_out', '')
    rack_id = request.GET.get('rack_id', -1)
    current_list = Current.objects.all()
    rack_list = Rack.objects.all()
    if request.method == 'POST':
        current_id = request.POST.get('current_id', '')
        quantity = int(request.POST.get('quantity', 0))
        rack_id = request.POST.get('rack_id', '')
        in_out = request.POST.get('in_out', '')
        if not all([current_id, quantity, rack_id, in_out]):
            return render(request, 'error_500.html', status=500)
        current = Current.objects.filter(id=current_id)
        rack = Rack.objects.filter(id=rack_id)
        if current.count() == 0 or rack.count() == 0 or quantity <= 0 or in_out not in ["入库", "出库"]:
            return render(request, 'error_500.html', status=500)
        remark = request.POST.get('remark', '')
        current = current.first()
        rack = rack.first()
        current_storage = CurrentStorage.objects.filter(current=current, rack=rack)
        if current_storage.count() > 0:
            current_storage = current_storage.first()
            if in_out == '入库':
                current_storage.quantity = current_storage.quantity + quantity
                CurrentRecord.objects.create(current=current, quantity=quantity, rack=rack, comment=remark, in_out=in_out, operating_user=request.user)
                current_storage.save()
            elif in_out == '出库':
                current_quantity = current_storage.quantity - quantity
                if current_quantity < 0:
                    return render(request, "warehousing.html", {'in_out': in_out, 'rack_id': int(rack_id),
                                                                  'current_list': current_list, 'rack_list': rack_list,
                                                                  "msg": "错误！出库数量大于库存数。"})
                elif current_quantity == 0:
                    current_storage.delete()
                    CurrentRecord.objects.create(current=current, quantity=quantity, rack=rack, comment=remark, in_out=in_out, operating_user=request.user)
                else:
                    current_storage.quantity = current_quantity
                    CurrentRecord.objects.create(current=current, quantity=quantity, rack=rack, comment=remark, in_out=in_out, operating_user=request.user)
                    current_storage.save()
        else:
            if in_out == '入库':
                CurrentStorage.objects.create(current=current, rack=rack, quantity=quantity)
                CurrentRecord.objects.create(current=current, quantity=quantity, rack=rack, comment=remark, in_out=in_out, operating_user=request.user)
            elif in_out == '出库':
                return render(request, "warehousing.html", {'in_out': in_out, 'rack_id': int(rack_id),
                                                            'current_list': current_list, 'rack_list': rack_list,
                                                            "msg": "错误！该物资无库存记录。"})
        return render(request, "warehousing.html", {'in_out': in_out, 'rack_id': int(rack_id),
                                                      'current_list': current_list, 'rack_list': rack_list,
                                                      "msg": "%s成功！" % in_out})
    else:
        return render(request, 'warehousing.html', {'in_out': in_out, 'rack_id': int(rack_id),
                                                    'current_list': current_list, 'rack_list': rack_list})
