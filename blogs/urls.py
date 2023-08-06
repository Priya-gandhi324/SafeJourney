from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_post', views.blog_post, name="blog_post"),
    path('subscribe', views.subscribe, name="subscribe")
]
