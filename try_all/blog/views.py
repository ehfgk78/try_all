from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post


def post_list(request):
    #1. 모든 블로그의 내용을 보여주기
    # posts = Post.objects.all()
    #2. published_date이 표시된 것만 보여주기
    # posts = Post.objects.filter(published_date__isnull=False)
    #3. published_date 순으로 보여주기
    # posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    #4. 최신 게시물부터 보여주기
    posts = Post.objects.filter(published_date__isnull=False)\
        .order_by('-published_date')
    context = {
        'posts': posts,
    }
    # view > url > 브라우저 랜더링 : 잘 동작하는지 확인
    # return HttpResponse("<h1> start view !!!</h1>")
    return render(request, 'blog/post_list.html', context)