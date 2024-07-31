from django.shortcuts import render, redirect
from news.models import New
from news.news_forms import NewsForm
from news.news_filters import NewsFilter
from django.contrib import messages
from django.views.generic import DetailView
from django.views import View

class NewsList(View):
    def get(self, request):
        news_queryset = New.objects.all()
        filter_object = NewsFilter(
            data=request.GET,
            queryset=news_queryset
        )

        context = {"filter_object": filter_object}
        return render(request, 'news_list.html', context)