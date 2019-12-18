"""WebApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from WebApp.views import Frontend
front=Frontend()

urlpatterns = [
   

    path('admin/', admin.site.urls),
]

urlpatterns += [

    path('web-security-checker/',  front.index, name='index'),
]


urlpatterns += [
    path('', RedirectView.as_view(url='web-security-checker/', permanent=True)),
    path('startprocess/', front.startprocess, name='startprocess'),
    path('ajax_SC/', front.ajax_SC, name='ajax-SC'),
    path('ajax_BL/', front.ajax_BL, name='ajax-BL'),
    path('ajax_BS/', front.ajax_BS, name='ajax-BS'),
   
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)