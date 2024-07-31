from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect


def user_lst(request):
    user_lst = User.objects.all()
    context = {"user_lst": user_lst}
    return render(request, 'user_lst.html', context)


