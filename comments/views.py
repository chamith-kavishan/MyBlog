from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=form.instance.post.pk)
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})
