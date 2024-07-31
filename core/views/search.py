from core.forms import *
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q



def search(request):
    keyword = request.GET["keyword"]
    # LIKE
    products = Product.objects.filter(
        Q(name__icontains=keyword) |
        Q(category__name__icontains=keyword)
    )
    context = {"products": products}
    return render(request, 'search_result.html', context)