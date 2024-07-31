from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect



def user_detail(request, id):
    user_info = User.objects.get(id=id)
    context = {"user": user_info}
    # if request.method == "GET":
    return render(request, 'user_detail.html', context)