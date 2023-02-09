from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

from .models import Post, Group


User = get_user_model()


NUM_POST_FOR_PAGE: int = 10

def index(request):
    """Вью для отображения главной страницы с публикациями"""
    template: str = 'posts/index.html'
    post_list = Post.objects.order_by('-pub_date')
    paginator = Paginator(post_list, NUM_POST_FOR_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context: dict = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Вью для отображения страниц с постами конкретной группы"""
    template: str = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(post_list, NUM_POST_FOR_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context: dict = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    template = 'posts/profile.html'
    user = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=user).order_by('-pub_date')
    post_count = post_list.count()
    paginator = Paginator(post_list, NUM_POST_FOR_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user': user,
        'page_obj': page_obj,
        'post_count': post_count,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = Post.objects.get(pk=post_id)
    author = post.author
    post_count = Post.objects.filter(author=author).count()
    context = {
        'post': post,
        'post_count': post_count
    }
    return render(request, template, context) 
