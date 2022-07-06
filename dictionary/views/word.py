from ..models import Word
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages


@require_http_methods(["GET"])
@login_required(login_url="signin")
def word_index(request):
    words = Word.objects.order_by("-id")[:10]
    return render(request, "word/index.html", {"words": words})


@login_required(login_url="signin")
@require_http_methods(["GET", "POST"])
def word_create(request):
    if request.method == "GET":
        return render(request, "word/create.html")

    elif request.method == "POST":
        language = request.POST["language"]

        if Word.objects.filter(language=language).exists():
            messages.info(request, "Word exists already")
            return redirect("dictionary:word.create")

        new_language = Word(language=language)
        new_language.save()
        return redirect("dictionary:word.index")


@login_required(login_url="signin")
@require_http_methods(["GET", "PUT"])
def word_edit(request, id):
    pass


@require_http_methods(["DELETE"])
@login_required(login_url="signin")
def word_delete(request, id):
    pass
