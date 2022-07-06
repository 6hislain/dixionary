from ..models import Language
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponse


@require_http_methods(["GET"])
@login_required(login_url="signin")
def language_index(request):
    languages = Language.objects.order_by("-id")[:10]
    return render(request, "language/index.html", {"languages": languages})


@require_http_methods(["GET"])
@login_required(login_url="signin")
def language_show(request, id):
    language = get_object_or_404(Language, pk=id)
    return render(request, "language/index.html", {"language": language})


@login_required(login_url="signin")
@require_http_methods(["GET", "POST"])
def language_create(request):
    if request.method == "GET":
        return render(request, "language/create.html")

    elif request.method == "POST":
        language = request.POST["language"]

        if Language.objects.filter(language=language).exists():
            messages.info(request, "Language exists already")
            return redirect("language:create")

        new_language = Language(language=language, user_id=request.user.id)

        if request.FILES.get("image") != None:
            new_language = Language(
                language=language,
                flag=request.FILES.get("image"),
                user_id=request.user.id,
            )

        new_language.save()
        messages.info(request, "Language created")

        return redirect("dictionary:language.index")


@login_required(login_url="signin")
@require_http_methods(["GET", "POST"])
def language_edit(request, id):
    language = get_object_or_404(Language, pk=id)

    if request.method == "GET":
        return render(request, "language/edit.html", {"language": language})

    elif request.method == "POST":
        language.language = request.POST["language"]

        if request.FILES.get("image") != None:
            language.flag = request.FILES.get("image")

        if request.user.id == language.user_id:
            language.save()
            messages.info(request, "Language updated")

        return redirect("dictionary:language.index")


@login_required(login_url="signin")
def language_delete(request, id):
    language = get_object_or_404(Language, pk=id)

    if request.user.id == language.user_id:
        language.delete()
        messages.info(request, "Language deleted")

    return redirect("dictionary:language.index")
