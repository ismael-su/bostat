
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='/auth/sign_in')
def dashboard_view(request: HttpRequest):
    rendered = render_to_string('dashboard/home.html', {'request': request})
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

