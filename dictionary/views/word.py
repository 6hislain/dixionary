from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from ..models import Word, Language


@require_http_methods(["GET"])
@login_required(login_url="signin")
def word_index(request):
    words = Word.objects.order_by("-id")[:10]
    return render(request, "word/index.html", {"words": words})


@require_http_methods(["GET"])
def word_show(request, slug):
    word = get_object_or_404(Word, slug=slug)
    return render(request, "word/index.html", {"word": word})


@login_required(login_url="signin")
@require_http_methods(["GET", "POST"])
def word_create(request):
    if request.method == "GET":
        languages = Language.objects.all()
        return render(request, "word/create.html", {"languages": languages})

    elif request.method == "POST":
        word = request.POST["word"]
        slug = slugify(word)
        language = request.POST["language"]
        new_word = Word(
            word=word, slug=slug, language_id=language, user_id=request.user.id
        )

        if request.FILES.get("image") != None:
            new_word = Word(
                word=word,
                slug=slug,
                language_id=language,
                user_id=request.user.id,
                image=request.FILES.get("image"),
            )

        new_word.save()
        messages.info(request, "Word created")
        return redirect("dictionary:word.index")


@login_required(login_url="signin")
@require_http_methods(["GET", "POST"])
def word_edit(request, id):
    word = get_object_or_404(Word, pk=id)

    if request.method == "GET":
        languages = Language.objects.all()
        return render(request, "word/edit.html", {"word": word, "languages": languages})

    elif request.method == "POST":
        word.word = request.POST["word"]
        word.slug = slugify(word.word)
        word.language_id = request.POST["language"]

        if request.FILES.get("image") != None:
            word.image = request.FILES.get("image")

        if request.user.id == word.user_id:
            word.save()
            messages.info(request, "Word updated")

        return redirect("dictionary:word.index")


@login_required(login_url="signin")
def word_delete(request, id):
    word = get_object_or_404(Word, pk=id)

    if request.user.id == word.user_id:
        word.delete()
        messages.info(request, "Word deleted")

    return redirect("dictionary:word.index")
