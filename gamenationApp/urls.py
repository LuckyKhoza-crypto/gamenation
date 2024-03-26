from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('import/', ImportTrafficSource.as_view(), name='import'),
    path('visual/', traffic_source_visual.as_view(), name='visual'),
    path('api/', traffic_source_api.as_view(), name='api'),

]
