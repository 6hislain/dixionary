from .auth import *
from .word import *
from .language import *
from .definition import *
from .translation import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from ..models import (
    Word,
    Profile,
    Language,
    Definition,
    DefinitionLike,
    Translation,
    TranslationLike,
)


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def stats(request):
    return render(request, "stats.html")


def profile(request, id):
    user = get_object_or_404(User, id=id)

    return HttpResponse(user)


@login_required(login_url="signin")
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == "GET":
        return render(request, "settings.html", {"user_profile": user_profile})

    if request.method == "POST":
        image = user_profile.image

        if request.FILES.get("image") != None:
            image = request.FILES.get("image")

        user_profile.image = image
        user_profile.bio = request.POST["bio"]
        user_profile.save()


@login_required(login_url="signin")
def dashboard(request):
    word_count = Word.objects.count()
    language_count = Language.objects.count()
    definition_count = Definition.objects.count()
    translation_count = Translation.objects.count()

    return render(
        request,
        "dashboard.html",
        {
            "word_count": word_count,
            "language_count": language_count,
            "definition_count": definition_count,
            "translation_count": translation_count,
        },
    )
