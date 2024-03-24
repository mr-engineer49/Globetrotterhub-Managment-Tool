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
    path('client/index_client/', include('campaignmanagment.urls')),
    path('client/index_client/', include('clientnmanagment.urls')),
    path('client/index_client/', include('offernmanagment.urls')),
    path('client/index_client/', include('reportsandanalytics.urls')),
    path('client/index_client/', include('bookingintegration.urls')),
    path('client/index_client/', include('sms.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

