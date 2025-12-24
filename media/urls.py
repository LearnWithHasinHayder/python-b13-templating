from django.urls import path
from .views import media

app_name='media'

urlpatterns = [
    path('hi/',media,name='say_hi')
]