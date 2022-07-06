from django.urls import path
from . import views

app_name = "dictionary"
urlpatterns = [
    path("word", views.word_index, name="word.index"),
    path("word/create", views.word_create, name="word.create"),
    path("word/<int:id>/edit", views.word_edit, name="word.edit"),
    path("word/<int:id>/delete", views.word_delete, name="word.delete"),
    path("language", views.language_index, name="language.index"),
    path("language/create", views.language_create, name="language.create"),
    path("language/<int:id>/edit", views.language_edit, name="language.edit"),
    path("language/<int:id>/delete", views.language_delete, name="language.delete"),
    path("language/<int:id>", views.language_show, name="language.show"),
    path("definition", views.definition_index, name="definition.index"),
    path("definition/create", views.definition_create, name="definition.create"),
    path("definition/<int:id>/edit", views.definition_edit, name="definition.edit"),
    path(
        "definition/<int:id>/delete", views.definition_delete, name="definition.delete"
    ),
    path("translation", views.translation_index, name="translation.index"),
    path("translation/create", views.translation_create, name="translation.create"),
    path("translation/<int:id>/edit", views.translation_edit, name="translation.edit"),
    path(
        "translation/<int:id>/delete",
        views.translation_delete,
        name="translation.delete",
    ),
]
