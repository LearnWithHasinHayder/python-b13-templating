from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="homex"),
    # path("/", views.home, name="homex"),
]
