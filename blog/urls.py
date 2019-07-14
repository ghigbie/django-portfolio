from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name="allblogs"),
    path('<int:blog_id>/'), view.blog_detail.html, name="blog_detail"),
]