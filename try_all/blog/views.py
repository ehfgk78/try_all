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


def post_detail(request, post_id):
    # <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
    # post_list.html 부분 중 위 a태그를 클릭하면 해당 post가 나타나도록 설계
    ## post.pk <-- 장고 Model Post <== 장고 ORM <<< DB기본키(Primary Key)
    ## post_id <--(views, 템플릿)- urls.py
    context = {
        'post' : Post.objects.get(pk=post_id)
    }
    return render(request, 'blog/post_detail.html', context)