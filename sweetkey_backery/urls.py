"""sweetkey_backery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from mainApp.views import CatView, SubCatView, ProdView

urlpatterns = [
    path('', CatView.as_view(), name = 'main_view'),
    path('cat/<str:name>', SubCatView.as_view(), name = 'cat_view'),
    path('scat/<str:name>', ProdView.as_view(), name = 'scat_view'),
    path('prod/<str:id>', ProdView.as_view(), name = 'prod_view'),
]
