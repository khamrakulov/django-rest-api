from django.urls import path
from .views import (
    get_or_create_users,
    user_detail,
)

urlpatterns = [
    path("users/", get_or_create_users, name="get_or_create_users"),
    path("users/<int:pk>", user_detail, name="user_detail"),
]