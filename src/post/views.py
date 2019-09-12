from django.shortcuts import render, get_object_or_404
from .models import Post, Shop
from django.urls import reverse


def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': latest,
        'featured': featured,
    }
    return render(request, 'index.html', context)


def blog(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
        'object_list': latest,
        'featured': featured
    }
    return render(request, 'blog.html', context)


def post(request, id):
    post = get_object_or_404(Post, id=id)
    base_url = reverse('post_list')
    context = {
        'post': post,
        'base_url': base_url
    }
    return render(request, 'post.html', context)


def help(request):
    return render(request, 'help.html', {})

def contact(request):
    return render(request, 'contact.html', {})


def shop(request):
    shop = Shop.objects.all()
    context = {
        "shop": shop
    }
    return render(request, 'shop.html', context)
