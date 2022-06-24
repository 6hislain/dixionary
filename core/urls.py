from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("stats", views.stats, name="stats"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("settings", views.settings, name="settings"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout, name="logout"),
]
