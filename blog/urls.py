from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('polls/<int:pk>/', views.home1, name='home1'),
    path('goto/', views.goto, name='goto'),
    path('ml/', views.my_likes, name='blog-like')
]




