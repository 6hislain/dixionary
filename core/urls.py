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
    path("profile/<int:id>", views.profile, name="profile"),
    path("language", views.language_index, name="language.index"),
    path("language/create", views.language_create, name="language.create"),
    path("language/<uuid:id>/edit", views.language_edit, name="language.edit"),
    path("language/<uuid:id>/delete", views.language_delete, name="language.delete"),
    path("word", views.word_index, name="word.index"),
    path("word/create", views.word_create, name="word.create"),
    path("word/<uuid:id>/edit", views.word_edit, name="word.edit"),
    path("word/<uuid:id>/delete", views.word_delete, name="word.delete"),
    path("definition", views.definition_index, name="definition.index"),
    path("definition/create", views.definition_create, name="definition.create"),
    path("definition/<uuid:id>/edit", views.definition_edit, name="definition.edit"),
    path(
        "definition/<uuid:id>/delete", views.definition_delete, name="definition.delete"
    ),
    path("translation", views.translation_index, name="translation.index"),
    path("translation/create", views.translation_create, name="translation.create"),
    path("translation/<uuid:id>/edit", views.translation_edit, name="translation.edit"),
    path(
        "translation/<uuid:id>/delete",
        views.translation_delete,
        name="translation.delete",
    ),
]
