from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"), #portfolio:home
    path("about/", views.about, name="about"), #portfolio:about
    path("contactxyz/", views.contact, name="contact"),
    path("project/", views.projects, name="projects"),
    path('contact-submission/',views.submission,name='contact-submission')
]
