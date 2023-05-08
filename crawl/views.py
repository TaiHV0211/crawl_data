from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from crawl.models import RealEstate


def real_estate_list(request, template_name='real_estate_list.html'):
    real_estate_list = RealEstate.objects.all().order_by("id")
    paginator = Paginator(real_estate_list, 20)
    pageNumber = request.GET.get('page')

    try:
        real_estate = paginator.page(pageNumber)
    except PageNotAnInteger:
        real_estate = paginator.page(1)
    except EmptyPage:
        real_estate = paginator.page(paginator.num_pages)
    data = {}
    data['real_estates'] = real_estate
    return render(request, template_name, data)


def real_estate_view(request, pk, template_name='real_estate_detail.html'):
    real_estate = RealEstate.objects.filter(id=pk)

    if real_estate:
        # real_estate = get_object_or_404(RealEstate, pk=pk)
        return render(request, template_name, {'real_estate': real_estate[0]})
    else:
        template_name = '404.html'
        return render(request, template_name)


def real_estate_search(request, template_name='real_estate_list.html'):
    min_price = request.GET.get('minPrices')
    max_price = request.GET.get('maxPrices')
    address = request.GET.get('address')

    queryset = RealEstate.objects.all()
    if min_price and max_price:
        queryset = queryset.filter(prices__range=(min_price, max_price))
    elif min_price:
        queryset = queryset.filter(prices__gte=min_price)
    elif max_price:
        queryset = queryset.filter(prices__lte=max_price)

    if address:
        queryset = queryset.filter(Q(address__icontains=address) | Q(agent_name__icontains=address))


    paginator = Paginator(queryset, 20)
    pageNumber = request.GET.get('page')

    try:
        real_estate = paginator.page(pageNumber)
    except PageNotAnInteger:
        real_estate = paginator.page(1)
    except EmptyPage:
        real_estate = paginator.page(paginator.num_pages)

    return render(request, template_name, {'real_estates': real_estate})
