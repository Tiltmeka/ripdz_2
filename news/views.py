from django.shortcuts import render
from .models import article
from django.http import HttpResponse


def news_home(request):
    news = article.objects.all()
    return HttpResponse("<h1>erwerewf</h1>")
