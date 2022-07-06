from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from dictionary.models import (
    Word,
    Profile,
    Language,
    Definition,
    Translation,
)

# Create your views here.


def index(request):
    return render(request, "index.html")


def stats(request):
    return render(request, "stats.html")


def profile(request, id):
    user = get_object_or_404(User, pk=id)

    return HttpResponse(user)


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")

    elif request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == "" or password != confirm_password:
            messages.info(request, "Passwords do not match")
            return redirect("signup")

        if email == "" or User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken")
            return redirect("signup")

        if username == "" or User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect("signup")

        new_user = User.objects.create_user(
            username=username, email=email, password=password
        )
        new_user.save()

        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)

        user_model = User.objects.get(email=email)
        new_profile = Profile.objects.create(user=user_model, my_user_id=user_model.id)
        new_profile.save()
        return redirect("dashboard")


@require_http_methods(["GET", "POST"])
def signin(request):
    if request.method == "GET":
        return render(request, "signin.html")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid credentials")
            return redirect("signin")

        auth.login(request, user)
        return redirect("dashboard")


@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    return redirect("/")


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
