from django.shortcuts import render, redirect
from news.models import New
from news.news_forms import NewsForm
from news.news_filters import NewsFilter
from django.contrib import messages
from django.views.generic import DetailView
from django.views import View


def news_search(request):
    keyword = request.GET["keyword"]
    # LIKE
    new = New.objects.filter(name__icontains=keyword)
    context = {"news": new}
    return render(request, 'search_result.html', context)