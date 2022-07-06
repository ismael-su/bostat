
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http.request import HttpRequest


# Create your views here.

def sign_in_view(request: HttpRequest):
    rendered = render_to_string('auth/sign_in.html', {'foo': 'bar'})
    return HttpResponse(rendered)

def sign_up_view(request: HttpRequest):
    rendered = render_to_string('auth/sign_up.html', {'foo': 'bar'})
    return HttpResponse(rendered)