from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, CommentForm
from .models import Post, PostComment


# Create your views here.


def post_list(request):
    # return HttpResponse('<h1>Start post_list</h1>')
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'post_list': posts,
        'comment_form': comment_form,
    }
    return render(request, 'instagram/post_list.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            post = Post.objects.create(
                photo=form.cleaned_data['photo'])
            return HttpResponse(f'<img src="{post.photo.url}">')
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'instagram/post_create.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    context = {
        'post': post,
        'common_form': comment_form,
    }
    return render(request, 'instagram/post_detail.html', context)


def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            PostComment.objects.create(
                post=post,
                content=form.cleaned_data['content']
            )
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('instagram:post_detail', post_id=post_id)