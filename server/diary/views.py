from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
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


def article_create(request):

    if request.method == 'GET':
        return render(request, 'diary/create.html')
    # 'POST'
    title = request.POST['title']
    content = request.POST['content']

    article = Article.objects.create(title=title, content=content)
    pk = article.id

    url = reverse('diary:article_read', kwargs={'pk': pk})
    return redirect(url)
