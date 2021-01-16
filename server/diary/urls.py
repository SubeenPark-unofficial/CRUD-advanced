from django.urls import path, include
from .views import *

app_name = 'diary'

urlpatterns = [
    path('', article_list, name="article_list"),
    path('article/<int:pk>/', article_read, name='article_read'),
    path('article/<int:pk>/update/', article_update, name='article_update'),
    path('article/<int:pk>/delete/', article_delete, name='article_delete'),
    path('article/create/', article_create, name='article_create'),
]
