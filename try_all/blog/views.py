from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import Post

User = get_user_model()


def post_list(request):
    # 1. 모든 블로그의 내용을 보여주기
    posts = Post.objects.all().order_by('-created_date')
    # 2. published_date이 표시된 것만 보여주기
    # posts = Post.objects.filter(published_date__isnull=False)
    # 3. published_date 순으로 보여주기
    # posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    # 4. 최신 게시물부터 보여주기
    # posts = Post.objects.filter(published_date__isnull=False) \
    #     .order_by('-published_date')
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

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return HttpResponse('No post', status=404)
    context = {
        # 'post': Post.objects.get(pk=post_id)
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    # return HttpResponse('<h1>Hello!!!</h1>')

    # base.html의 '추가 +' 버튼을 누르면, post_add.html페이지로 이동
    # title, content 작성 후 '발행'여부를 체크하고 '작성하기'버튼을 누르면
    # post_detail.html로 이동하여 작성한 글을 확인하기
    ## author 작성자는 get_user_model()에서 가져오기
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_publish = bool(request.POST.get('is_publish'))
        author = User.objects.get(username='learn')

        # title & content 모두 작성할 때에만 Post 생성
        if title and content:
            post = Post.objects.create(
                author=author,
                title=title,
                content=content,
            )
            # 발행여부 체크 >> 저장되지만 게시되지 않음 post_list
            if is_publish:
                post.publish()
            else:
                post.save()
            # post_detail.html로 가기 (url을 거쳐서)
            return redirect('post_detail', post_id=post.pk)

        # title이나 content를 기입하지 않았다면
        # 기입한 항목만 post_add.html에 전달하면서 이동
        context = {
            'title': title,
            'content': content,
        }
    else:
        context = {}
    return render(request, 'blog/post_add.html', context)

def post_delete(request, post_id):
    # post_detail.html에서 글 삭제 버튼 추가
    # 삭제하면 해당 post를 DB에서 삭제하고
    # post_list.html로 이동
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('post_list')
    return HttpResponse('삭제가 거부되었습니다.', status=403)
