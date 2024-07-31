from django.shortcuts import render, redirect
from news.models import New
from news.news_forms import NewsForm
from news.news_filters import NewsFilter
from django.contrib import messages
from django.views.generic import DetailView
from django.views import View


class NewDetailView(View):
    def get(self, request, pk):
        new_object = New.objects.get(pk=pk)
        new_object.views += 1
        if request.user.is_authenticated:
            new_object.user_views.add(request.user)
        new_object.save()
        context = {
            "new": new_object,
        }
        return render(request, 'news_detail.html', context)