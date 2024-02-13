from django.urls import path, include
from .views import authView, home, dashboard, algorithme

urlpatterns = [
 path("", home, name="home"),
 path("dashboard/", dashboard, name="dashboard"),
 path("algorithme/", algorithme, name="algorithme"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
]
