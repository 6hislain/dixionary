from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Definition, Word


@require_http_methods(["GET"])
@login_required(login_url="signin")
def definition_index(request):
    definitions = Definition.objects.order_by("-id")[:10]
    return render(request, "definition/index.html", {"definitions": definitions})

@login_required(login_url="signin")
@require_http_methods(["GET", "POST"])
def definition_create(request, word_id):
    word = get_object_or_404(Word, pk=word_id)

    if request.method == "GET":
        return render(request, "definition/create.html", {"word": word})

    elif request.method == "POST":
        definition = request.POST["definition"]

        new_definition = Definition(
            word=word, definition=definition, user_id=request.user.id
        )
        new_definition.save()
        return redirect("dictionary:definition.index")

@login_required(login_url="signin")
@require_http_methods(["GET", "POST"])
def definition_edit(request, id):
    pass


@require_http_methods(["DELETE"])
def definition_delete(request, id):
    pass
