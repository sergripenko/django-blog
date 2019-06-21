from django.shortcuts import render, redirect
from .forms import CommentsForm, PostForm
from .models import Comments, Post


def post_list(request):
    posts = Post.objects.all()
    form = PostForm()

    return render(request, 'blog/base.html', {'posts': posts, 'form': form})


def get_comm(request):
    if request.method == 'POST':
        bound_form = request.POST
        if bound_form.get('post-id') and bound_form.get('post-id').isnumeric():
            post=Post.objects.filter(pk=int(bound_form.get("post-id")))
            if len(post) == 0:
                return redirect('post_list')
        else:
            return redirect('post_list')
        new_comment = Comments(author=request.user,massage=bound_form.get('message'),
                        answer_massage=post[0])
        new_comment.save()
        return redirect('post_list')


def get_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_list')
        return redirect('post_list', {'error': 'какая-то невдача'})


def get_comm_on_comm(request):
    if request.method == 'POST':
        bound_form = request.POST
        if bound_form.get('comm-id') and bound_form.get('comm-id').isnumeric():
            comm=Comments.objects.filter(pk=int(bound_form.get("comm-id")))
            if len(comm) == 0:
                return redirect('post_list')
        else:
            return redirect('post_list')
        new_comment = Comments(author=request.user,massage=bound_form.get('comm-message'),
                        answer_comment=comm[0])
        new_comment.save()
        return redirect('post_list')