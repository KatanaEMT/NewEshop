from django.shortcuts import render, redirect
from news.models import New
from news.news_forms import NewsForm
from news.news_filters import NewsFilter
from django.contrib import messages
from django.views.generic import DetailView
from django.views import View


def new_create(request):
    if request.method == "GET":
        return render(request, 'new_create.html')
    elif request.method == "POST":
        # считывание данных с формы
        data = request.POST
        title = data["new_title"]
        text = data["new_article"]


        # сохрание этих данных в
        new_object = New.objects.create(
            title=title,
            article=text,
        )
        messages.success(request, "Вы успешно создали новость")
        return redirect(f'/news-detail/{new_object.id}/')