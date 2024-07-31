from django.shortcuts import render, redirect, HttpResponse
from .models import Costumer, Profile
from core.forms import ProfileForm
from django.contrib import messages
from django.views.generic import DetailView
from django.views import View



def costumer_view(request):
    costumer_list = Costumer.objects.all()
    context = {"costumer_list": costumer_list}
    return render(request, 'costumers.html', context)


def profile(request):
    profile_list = Profile.objects.all()
    context = {"profile": profile_list}
    return render(request, 'profile_lst.html', context)


def profile_detail(request, id):
    profile_info = Profile.objects.get(id=id)
    context = {"profile": profile_info}
    # if request.method == "GET":
    return render(request, 'profile_detail.html', context)


def costumers_create(request):
    if request.method == "GET":
        return render(request, 'costumers_create.html')
    elif request.method == "POST":
        # считывание данных с формы
        data = request.POST
        name = data["new_name"]
        age = data["new_age"]
        gender = data["new_gender"]
        # user = data["user"]


        # сохрание этих данных в
        new_object = Costumer.objects.create(
            name=name,
            age=age,
            gender=gender,
            # user=user
        )
        messages.success(request, "Профиль покупателя успешно создан!")
        return redirect(f'/costumers/')


class ProfileCreateView(View):
    def get(self, request):
        context = {}
        context["profile_form"] = ProfileForm()
        return render(request, 'profile_create.html', context)

    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Вы успешно создали профиль")
            return redirect('/')
        return HttpResponse("Ошибка валидации!")


def profile_update(request, id):
    context = {}
    profile_object = Profile.objects.get(id=id)
    context["profile_form"] = ProfileForm(instance=profile_object)

    if request.method == "GET":
        return render(request, 'profile/update.html', context)
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile_object)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Профиль обновлен")
            return redirect('/')
        return HttpResponse("Ошибка валидации!")