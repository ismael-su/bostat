
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.http.request import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #import messages


from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    
# Create your views here.

def sign_in_view(request: HttpRequest):
    

    
    if request.method == 'POST':
        print('PST')
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "You have logged in!")
                    return redirect(request.GET.get('next'))

            else:
                messages.warning(request, "Your account is disabled!")
                
        
    else:
        print('GET')
        form = SignInForm()
        
    rendered = render_to_string('auth/sign_in.html', {'form': form})
    return HttpResponse(rendered)

def sign_up_view(request: HttpRequest):
    rendered = render_to_string('auth/sign_up.html', {'foo': 'bar'})
    return HttpResponse(rendered)


def sign_out_view(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect('/')
    