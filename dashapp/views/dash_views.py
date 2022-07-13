
from cProfile import label
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from dashapp.models import (
    Marque
)


# Create your views here.

@login_required(login_url='/auth/sign_in')
def dashboard_view(request: HttpRequest):
    
    marque_labels = []
    marque_data = []
    
    

    
    marque_queryset = Marque.objects.all()[:5]
    for marque in marque_queryset:
        marque: Marque
        marque_labels.append(marque.nomarque)
        # count = 
        marque_data.append(10)

    rendered = render_to_string(
        'dashboard/home.html', 
        {
            'request': request,
            'labels': marque_labels,
            'data':marque_data,
            'table_dataset': marque_queryset
        }
    )
    return HttpResponse(rendered)

@login_required(login_url='/auth/sign_in')
def customer_view(request: HttpRequest):
    rendered = render_to_string('dashboard/customer.html', {'request': request})
    return HttpResponse(rendered)

@login_required(login_url='/auth/sign_in')
def operation_view(request: HttpRequest):
    rendered = render_to_string('dashboard/operation.html', {'request': request})
    return HttpResponse(rendered)

@login_required(login_url='/auth/sign_in')
def products_view(request: HttpRequest):
    rendered = render_to_string('dashboard/products.html', {'request': request})
    return HttpResponse(rendered)

