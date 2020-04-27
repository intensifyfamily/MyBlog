from django.urls import path
from . import  views
app_name = 'blog'

urlpatterns = [
    path('<str:userId>/article', views.Articles.as_view(), name='博文'),
    path('article/<str:articleId>/comment', views.Comment.as_view(), name='评论'),
    path('article/<str:articleId>/reply', views.Reply.as_view(), name='回复'),
]
