import numpy as np
import pandas as pd
from django.shortcuts import render
from flexible.models import LoadSheet, LoadSheetContent


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
        del(params['csrfmiddlewaretoken'])
        del (params['load_sheet_id'])
        data = {}
        data.setdefault('旅客', {})
        data.setdefault('行李', {})
        data.setdefault('其他', {})
        for param_name, param_value in params.items():
            type_, id_, name = param_name.split('_')
            if type_ == 'fixPax':
                data['旅客'].setdefault(id_, {})
                data['旅客'][id_][name] = param_value
            elif type_ == 'fixBaggage':
                data['行李'].setdefault(id_, {})
                data['行李'][id_][name] = param_value
            elif type_ == 'fixOther':
                data['其他'].setdefault(id_, {})
                data['其他'][id_][name] = param_value
        load_sheet_content = LoadSheetContent.objects.filter(load_sheet__id=load_sheet_id)
        total_score = 0
        lcm_total = 0
        passenger_correct = False
        baggage_correct = False
        other_correct = False
        passenger, baggage, other = [pd.DataFrame(None)] * 3
        for key, value in data.items():
            df = pd.DataFrame(value).T
            if key == '旅客':
                load_sheet_passenger = load_sheet_content.filter(project='旅客')
                if df.shape[0] > 0:
                    df['paxNumber'] = df['paxNumber'].apply(int)
                    df['paxWeight'] = df['paxWeight'].apply(int)
                    df = df.pivot_table(values=['paxNumber', 'paxWeight'], index=['destination', 'paxClass', 'paxType'], dropna=False, margins=True, margins_name='合计', aggfunc=np.sum)
                    lcm_total += df.loc['合计', '', '']['paxWeight']
                    passenger = df
                    correct = False
                    if load_sheet_passenger.count() == df.shape[0]-1:
                        correct = True
                        for obj in load_sheet_passenger:
                            try:
                                if df.loc[obj.destination, obj._class, obj.type]['paxNumber'] == obj.number and df.loc[obj.destination, obj._class, obj.type]['paxWeight'] == obj.weight:
                                    continue
                                else:
                                    correct = False
                                    break
                            except:
                                correct = False
                                break
                else:
                    correct = True if load_sheet_passenger.count() == 0 else False
                if correct:
                    total_score += 33.33
                    passenger_correct = True
            elif key == '行李':
                load_sheet_baggage = load_sheet_content.filter(project='行李')
                if df.shape[0] > 0:
                    df['baggageNumber'] = df['baggageNumber'].apply(int)
                    df['baggageWeight'] = df['baggageWeight'].apply(int)
                    df = df.pivot_table(values=['baggageNumber', 'baggageWeight'], index=['destination', 'baggageLocation'], dropna=False, margins=True, margins_name='合计', aggfunc=np.sum)
                    lcm_total += df.loc['合计', '']['baggageWeight']
                    baggage = df
                    correct = False
                    if load_sheet_baggage.count() == df.shape[0]-1:
                        correct = True
                        for obj in load_sheet_baggage:
                            try:
                                if df.loc[obj.destination, obj.location]['baggageNumber'] == obj.number and df.loc[obj.destination, obj.location]['baggageWeight'] == obj.weight:
                                    continue
                                else:
                                    correct = False
                                    break
                            except:
                                correct = False
                                break
                else:
                    correct = True if load_sheet_baggage.count() == 0 else False
                if correct:
                    total_score += 33.33
                    baggage_correct = True
            elif key == '其他':
                load_sheet_other = load_sheet_content.filter(project='其他')
                if df.shape[0] > 0:
                    df['weight'] = df['weight'].apply(int)
                    df = df.pivot_table(values=['weight'], index=['destination', 'location', 'type'], dropna=False, margins=True, margins_name='合计', aggfunc=np.sum)
                    other = df
                    lcm_total += df.loc['合计', '', '']['weight']
                    correct = False
                    if load_sheet_other.count() == df.shape[0] - 1:
                        correct = True
                        for obj in load_sheet_other:
                            try:
                                if df.loc[obj.destination, obj.location, obj.type]['weight'] == obj.weight:
                                    continue
                                else:
                                    correct = False
                                    break
                            except:
                                correct = False
                                break
                else:
                    correct = True if load_sheet_other.count() == 0 else False
                if correct:
                    total_score += 33.33
                    other_correct = True
        total_score = round(total_score, 0)
        return render(request, 'view_loadsheet.html', {'total_score': total_score, 'lcm_total': lcm_total,
                                                       'passenger': passenger, 'baggage': baggage, 'other': other,
                                                       'passenger_correct': passenger_correct,
                                                       'baggage_correct': baggage_correct,
                                                       'other_correct': other_correct})
    else:
        return render(request, 'error_403.html', status=403)
