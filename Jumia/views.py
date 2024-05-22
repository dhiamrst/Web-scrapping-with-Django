from django.shortcuts import render
import csv
from .models import Smartphone

def page1(request):
    smartphones = Smartphone.objects.all()
    brands = Smartphone.objects.values('brand').distinct()
    min_price = request.GET.get('minPrice', None)
    max_price = request.GET.get('maxPrice', None)
    selected_brand = request.GET.get('brand', '')
    smartphones = Smartphone.objects.all()
    if min_price is not None and min_price != '':
        smartphones = smartphones.filter(price__gte=min_price)
    if max_price is not None and max_price != '':
        smartphones = smartphones.filter(price__lte=max_price)
    if selected_brand:
        smartphones = smartphones.filter(brand=selected_brand)

    context={
        'smartphones':smartphones,
        'brands':brands,
        'min_price': min_price,
        'max_price': max_price,
        'selected_brand': selected_brand
    }

    return render(request, 'Jumia/page1.html', context)
