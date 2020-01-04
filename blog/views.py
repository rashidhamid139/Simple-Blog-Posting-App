from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Post_like
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context )


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

'''
from django.shortcuts import render, redirect
from . models import Post, Post_like, User


def home1(request, pk):
    user_id = 3
    post_id = pk
    post_l = Post_like.objects.all().values_list('u_id', 'p_id')
    liik = (user_id, post_id)
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
def goto(request):
    posts = Post.objects.all()
    return render(request, 'polls/home.html', {'posts': posts})



def my_likes(request):
    user_id = 7
    posts = Post_like.objects.filter(u_id = user_id).values_list('p_id', flat=True)
    posts = Post.objects.filter(pk__in=posts)

    return render(request, 'polls/goto.html', {'posts': posts})

'''