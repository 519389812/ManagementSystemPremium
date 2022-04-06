from django.shortcuts import render
from quickcheck.models import Province, City


def quickcheck(request):
    provinces = list(Province.objects.all().values_list('name', flat=True))
    city_contents = {}
    cities = City.objects.all()
    for province in provinces:
        city_contents[province] = cities.filter(province__name=province)
    for queryset in city_contents.values():
        for query in queryset:
            query.policy = {v.split('-')[0]: v.split('-')[1:] for v in query.policy.split('*') if v != ''}
    last_update_datetime = cities.order_by('-update_datetime').first().update_datetime
    return render(request, 'quickcheck.html', {'city_contents': city_contents, 'last_update_datetime': last_update_datetime})
