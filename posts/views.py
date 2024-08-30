from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Bookmark
from .forms import PostForm
from comments.forms import CommentForm
from django.template.defaultfilters import truncatechars
from django.core.paginator import Paginator
from django.contrib import messages

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for post in page_obj.object_list:
        post.content = truncatechars(post.content, 100)
    context = {'page_obj': page_obj}
    return render(request, "posts/post_list.html", context)

@login_required
def user_post_list(request):
    user = request.user
    posts = Post.objects.filter(author=user).order_by('-created_at')
    for post in posts:
        post.content = truncatechars(post.content, 100)
    context = {'post_list': posts}
    return render(request, "posts/user_post_list.html", context)

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    is_bookmarked = post.is_bookmarked_by(request.user)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', id=post.id)  # Redirect back to post detail page
    else:
        comment_form = CommentForm()
    return render(request, "posts/post_detail.html", {'post': post, 'comments': comments, 'comment_form': comment_form, 'is_bookmarked': is_bookmarked})

@login_required
def post_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = PostForm()
        else:
            post = Post.objects.get(pk=id)
            form = PostForm(instance=post)
        return render(request, "posts/post_form.html", {'form': form})
    elif request.method == 'POST':
        if id == 0:
            form = PostForm(request.POST, request.FILES)
            form.instance.author = request.user
        else:
            post = Post.objects.get(pk=id)
            form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post saved successfully.')
            return redirect('/posts/user_posts/')
        else:
            messages.error(request, 'Failed to save post. Please check the form.')
            return render(request, "posts/post_form.html", {'form': form})

@login_required
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    if post:
        post.delete()
        messages.success(request, 'Post deleted successfully.')
    else:
        messages.error(request, 'Failed to delete post.')
    return redirect('/posts/user_posts/')

@login_required
def bookmark_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if Bookmark.objects.filter(user=user, post=post).exists():
        Bookmark.objects.filter(user=user, post=post).delete()
        messages.success(request, 'Bookmark removed successfully.')
    else:
        Bookmark.objects.create(user=user, post=post)
        messages.success(request, 'Bookmark added successfully.')
    return redirect('post_detail', id=post_id)

@login_required
def bookmarked_posts(request):
    user = request.user
    bookmarked_posts = Bookmark.objects.filter(user=user).select_related('post')
    for bookmark in bookmarked_posts:
        bookmark.post.content = truncatechars(bookmark.post.content, 100)
    paginator = Paginator(bookmarked_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, "posts/bookmarked_posts.html", context)