"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from apps.cars import api as car_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include('apps.docs.urls')),
    path('cars/', car_api.CarListCreateApi.as_view(), name='api_create_list_car'),
    path('rate/', car_api.RatingCreateApi.as_view(), name='api_create_rating'),
    path('popular/', car_api.CarPopularityApi.as_view(), name='api_list_car_popularity'),
]

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns.append(path('api/__debug__/', include(debug_toolbar.urls)))
    except ModuleNotFoundError:
        print('Django debug toolbar disabled')
