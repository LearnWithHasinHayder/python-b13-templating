from django.urls import path
from . import views

app_name = "ecommerce"

urlpatterns = [
    path("check/<int:n>", views.num, name="odd_even"),
    path("record/<str:name>/<int:age>", views.record, name="record"),
    path("show/", views.show, name="show"),
    path("users/", views.UserView.as_view(), name="users_view"),
    path("users/<int:id>", views.UserDetailView.as_view(), name="user_view"),
    path('json_users/', views.json_users, name='json_users'),
    path('json_users/<int:id>', views.json_single_user, name='json_users')
]

# GET POST PUT PATCH DELETE

#  /users GET POST 
#  /users/1 GET PUT PATCH DELETE