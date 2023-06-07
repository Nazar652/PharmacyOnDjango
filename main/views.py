from django.shortcuts import render

from .models import *


def index(request):
    most_valuable = Drug.objects.order_by('-price')[:4]
    return render(request, 'main/index.html', {'most_valuable': most_valuable})


def catalog(request):
    list_of_drugs = Drug.objects.all()
    return render(request, 'main/catalog.html', {'list_of_drugs': list_of_drugs})


def about_us(request):
    return render(request, 'main/about_us.html')


def page(request, ident):
    drug = Drug.objects.get(pk=ident)
    return render(request, 'main/page.html', {'drug': drug})
