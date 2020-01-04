from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Post_like
from django.contrib.auth.models import User

from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


# def home(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/home.html', context )



class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



def home1(request, pk):
    user_id = request.user.id
    post_id = pk
    post_l = Post_like.objects.all().values_list('u_id', 'p_id')
    liik = (user_id, post_id)
    if user_id is not None:
        if liik in post_l:
            Post_like.objects.get(u_id = user_id, p_id= post_id).delete()
            a = Post.objects.get(pk=post_id)
            a.count = a.count - 1
            a.save()
            return redirect('blog-home')
        else:
            Post_like.objects.create(u_id=user_id, p_id=post_id)
            a = Post.objects.get(pk=post_id)
            a.count = a.count + 1
            a.save()
            return redirect('blog-home')
    else:
        return redirect('login')
def goto(request):
    posts = Post.objects.all()
    return render(request, 'polls/home.html', {'posts': posts})



def my_likes(request):
    user_id = request.user.id
    print(user_id)
    posts = Post_like.objects.filter(u_id = user_id).values_list('p_id', flat=True)
    posts = Post.objects.filter(pk__in=posts)

    return render(request, 'blog/goto.html', {'posts': posts})
