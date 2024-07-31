from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.forms import *
from django.contrib import messages


def signin(request):
    context = {}

    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                messages.success(request, "Вы успешно авторизовались")
                return redirect('/')
            messages.warning(request, "Логин и/или пароль неверны")

    form = AuthForm()
    context["form"] = form
    return render(request, "start/signin.html", context)