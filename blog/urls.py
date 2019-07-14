from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name="allblogs"),
<<<<<<< HEAD
    path('<int:blog_id>/', views.blog_detail, name="blog_detail"),
=======
    path('<int:blog_id>/', views.detail, name='detail'),
>>>>>>> 8bc3d9c71039f5f5d7f427a49f538889a9175996
]