from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.forms import *
from core.filters import ProductFilter


def registration(request):
    context = {}

    if request.method == "POST":
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            user_object = reg_form.save()
            password = request.POST["password"]
            user_object.set_password(password)
            user_object.save()
            return redirect('/')
        return HttpResponse("Ошибка валидации")

    reg_form = RegistrationForm()
    context["reg_form"] = reg_form
    return render(request, "start/registration.html", context)