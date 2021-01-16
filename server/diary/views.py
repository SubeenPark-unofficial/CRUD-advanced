from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'diary/list.html', context=context)


def article_read(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, 'diary/read.html', context=context)
