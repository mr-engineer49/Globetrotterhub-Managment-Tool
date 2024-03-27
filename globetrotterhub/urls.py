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
    path('admin-page/', include('dashboard.urls')),
    path('admin-page/campaign-managment/', include('campaignmanagment.urls')),
    path('admin-page/client-managment/', include('clientnmanagment.urls')),
    path('admin-page/offer-managment/', include('offernmanagment.urls')),
    path('admin-page/reports-and-analytics/', include('reportsandanalytics.urls')),
    path('admin-page/booking-integration/', include('bookingintegration.urls')),
    path('admin-page/conversations/', include('sms.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

