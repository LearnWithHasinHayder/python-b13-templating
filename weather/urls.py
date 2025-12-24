from django.urls import path
from . import views
app_name = 'weather'

urlpatterns = [
    path('dhaka/',views.dhaka,name='dhaka_weather'),
    path('rajshahi/',views.rajshahi,name='rajshahi_weather'),    
    path('intro/',views.intro ,name='intro'),    
]
