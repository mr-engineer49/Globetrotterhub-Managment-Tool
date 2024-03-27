"""
URL configuration for globetrotterhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name='campaignmanagment'

urlpatterns = [
    path('campaigns-view/', views.campaigns_view, name="campaigns_form"),
    path('new/', views.new_campaign_view, name="new_campaign"),
    path('campaigns/<int:pk>/', views.campaign_detail_view, name='campaign_detail'),
    path('campaigns/<int:pk>/edit/', views.edit_campaign_view, name='edit_campaign'),
    path('campaigns/<int:pk>/delete/', views.delete_view, name='delete_campaign'),
    
]
