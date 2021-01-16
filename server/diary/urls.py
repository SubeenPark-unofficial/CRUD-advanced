from django.urls import path, include
from .views import *

app_name = 'diary'

urlpatterns = [
    path('', article_list, name="article_list"),
]
