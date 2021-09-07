from django.contrib import admin
from performance.views import get_queryset
from django.contrib import messages
from django.shortcuts import render, redirect
from ManagementSystemPremium.views import parse_url_param


class PersonSummaryAdmin(admin.ModelAdmin):
    change_list_template = "admin/workload_summary_change_list.html"

    # list_filter = (
    #     ('start_datetime', DateTimeRangeFilter), 'user__team', 'position__type', 'position'
    # )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)

        url = request.META.get('HTTP_REFERER', '')
        if url == '':
            return render(request, 'error_400.html', status=400)
        url_params = parse_url_param(url)
        workload_queryset = get_queryset(url_params, 'WorkloadRecord')
        if workload_queryset.count() == 0:
            messages.error(request, '无数据')
            messages.set_level(request, messages.ERROR)
            return redirect(url)

        try:
            qs =
        except (AttributeError, KeyError):
            return response
        metrics = {
            'count': Count('user'),
            'number_people': Sum('number_people'),
            'number_baggage': Sum('number_baggage'),
            'sale': Sum('sale'),
        }
        response.context_data['summary'] = list(
            qs.filter(verified=True).values('user__team__name').values('user__full_name').annotate(**metrics).order_by('-sale')
        )
        return response
