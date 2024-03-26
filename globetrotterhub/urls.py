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
from globetrotterhub import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('homepage.urls')),
    path('auth/', include('registration.urls')),
    path('client/', include('dashboard.urls')),
    path('client/campaign_managment/', include('campaignmanagment.urls')),
    path('client/client_managment/', include('clientnmanagment.urls')),
    path('client/offer_managment/', include('offernmanagment.urls')),
    path('client/reports_and_analytics/', include('reportsandanalytics.urls')),
    path('client/booking_integration/', include('bookingintegration.urls')),
    path('client/conversations/', include('sms.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

