"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


from dashapp.views.auth_views import sign_in_view, sign_up_view, sign_out_view
from dashapp.views.dash_views import customer_view, dashboard_view, operation_view, products_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dashboard', view=dashboard_view, name='Dashboard'),
    path('Products', view=products_view, name='Products'),
    path('Customer', view=customer_view, name='Customer'),
    path('Operation', view=operation_view, name='Operation'),
    path('auth/sign_in', name='sign_in', view=sign_in_view),
    path('auth/sign_up', name='sign_up', view=sign_up_view),
    path('auth/sign_out', name='sign_out', view=sign_out_view),
    path("__reload__/", include("django_browser_reload.urls")),
    re_path(r'^.*$', RedirectView.as_view(url='Dashboard', permanent=False), name='index')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
