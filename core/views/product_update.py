from django.shortcuts import render, HttpResponse, redirect
from core.models import *
from core.forms import *
from core.filters import ProductFilter
from django.contrib import messages


def product_update(request, id):
    context = {}
    product_object = Product.objects.get(id=id)
    context["product_form"] = ProductForm(instance=product_object)

    if request.method == "GET":
        return render(request, 'product/update.html', context)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, instance=product_object)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Вы успешно обновили")
            return redirect('/')
    return HttpResponse("Ошибка валидации!")