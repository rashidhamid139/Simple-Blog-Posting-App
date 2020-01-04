from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('polls/<int:pk>/', views.home1, name='home1'),
    path('goto/', views.goto, name='goto'),
    path('ml/', views.my_likes, name='blog-like')
]




