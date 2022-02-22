def return_get_queryset_by_team(request, qs, field_name):
    if not request.user.is_superuser:
        try:
            qs = eval("qs.filter(%s__in=[request.user.team])" % field_name)
        except:
            pass
    return qs


def return_get_queryset_by_related_team(request, qs, field_name):
    if not request.user.is_superuser:
        team = request.user.team
        try:
            while True:
                if team.parent:
                    team = team.parent
                    continue
                else:
                    qs = eval("qs.filter(%s__in=[team])" % field_name)
                    break
        except:
            pass
    return qs


def return_get_queryset_by_parent_team(request, qs, field_name):
    if not request.user.is_superuser:
        try:
            if request.user.team.parent:
                qs = eval("qs.filter(%s__in=[request.user.team.parent])" % field_name)
            else:
                qs = eval("qs.filter(%s__in=[request.user.team])" % field_name)
        except:
            pass
    return qs


def return_get_queryset_by_parent_team_foreignkey(request, qs, field_name):
    if not request.user.is_superuser:
        try:
            if request.user.team.parent:
                team_id = request.user.team.parent.id
            else:
                team_id = request.user.team.id
            qs = eval("qs.filter(%s__related_parent__iregex=r'[^0-9]*%s[^0-9]')" % (field_name, str(team_id)))
        except:
            pass
    return qs
