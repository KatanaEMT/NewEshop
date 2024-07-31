from django.shortcuts import render, HttpResponse, redirect
from core.models import *
from core.forms import ProductForm
from core.filters import ProductFilter
from django.contrib import messages



def product_create(request):
    context = {}
    context["product_form"] = ProductForm()

    if request.method == "GET":
        return render(request, 'product_create.html', context)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Вы успешно создали товар")
            return redirect('/')
        return HttpResponse("Ошибка валидации!")