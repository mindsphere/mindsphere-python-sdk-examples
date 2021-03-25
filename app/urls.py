"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin


# Admin Site Config
admin.sites.AdminSite.site_header = 'SDK E2E Testing App'
admin.sites.AdminSite.site_title = 'SDK Admin'
admin.sites.AdminSite.index_title = 'SDK Admin index'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assets.urls')),
    path('', include('tokentype.urls')),
    path('', include('events.urls')),
    path('', include('fileservice.urls')),
    path('', include('iotbulk.urls')),
    path('', include('iottimeseries.urls')),
    path('', include('iottsaggregate.urls')),
    path('', include('mindconnectapi.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
