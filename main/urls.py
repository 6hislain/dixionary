from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", TemplateView.as_view(template_name="about.html"), name="about"),
    path("stats", views.stats, name="stats"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("settings", views.settings, name="settings"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout, name="logout"),
    path("profile/<int:id>", views.profile, name="profile"),
]
