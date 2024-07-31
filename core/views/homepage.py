from django.shortcuts import render, HttpResponse, redirect
from core.models import *
from core.filters import *
from core.forms import *


def homepage(request):
    # SELECT * FROM Product;
    product_list = Product.objects.all()
    filter_object = ProductFilter(
        data=request.GET,
        queryset=product_list
    )

    context = {"filter_object": filter_object}
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html', context)