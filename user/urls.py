from django.urls import path
from .views import Health, LoginView, register, getAll

urlpatterns = [
    path("", Health, name="Health"),
    path("login", LoginView.as_view(), name="login"),
    path("register", register, name="register"),
    path("get", getAll, name="get"),
]
