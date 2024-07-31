from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect


def signout(request):
    logout(request)
    return redirect('/')