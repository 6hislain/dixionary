from ..models import Translation, Definition, Language
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages


@require_http_methods(["GET"])
@login_required(login_url="signin")
def translation_index(request):
    translations = Translation.objects.order_by("-id")[:10]
    return render(request, "translation/index.html", {"translations": translations})


@login_required(login_url="signin")
@require_http_methods(["GET", "POST"])
def translation_create(request, definition_id):
    definition = get_object_or_404(Definition, pk=definition_id)

    if request.method == "GET":
        languages = Language.objects.all()
        return render(
            request,
            "translation/create.html",
            {"definition": definition, "languages": languages},
        )

    elif request.method == "POST":
        word = request.POST["word"]
        language = request.POST["language"]
        translation = request.POST["translation"]

        new_translation = Translation(
            word=word,
            translation=translation,
            definition_id=definition.id,
            language_id=language,
            user_id=request.user.id,
        )
        new_translation.save()
        messages.info(request, "Translation created")
        return redirect("dictionary:translation.index")


@login_required(login_url="signin")
@require_http_methods(["GET", "POST"])
def translation_edit(request, id):
    translation = get_object_or_404(Translation, pk=id)

    if request.method == "GET":
        languages = Language.objects.all()
        return render(
            request,
            "translation/edit.html",
            {"languages": languages, "translation": translation},
        )

    elif request.method == "POST":
        translation.word = request.POST["word"]
        translation.language_id = request.POST["language"]
        translation.translation = request.POST["translation"]
        translation.definition_id = translation.definition_id

        if request.user.id == translation.user_id:
            translation.save()
            messages.info(request, "Translation updated")

        return redirect("dictionary:translation.index")


@login_required(login_url="signin")
def translation_delete(request, id):
    translation = get_object_or_404(Translation, pk=id)

    if request.user.id == translation.user_id:
        translation.delete()
        messages.info(request, "Translation deleted")

    return redirect("dictionary:translation.index")
