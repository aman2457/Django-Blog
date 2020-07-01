from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Comment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts, 4)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_lists = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_lists = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_lists = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'page': page,'post_lists': post_lists})



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.post_views += 1
    post.save()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_details.html', {'form': form, 'post': post})


    
    '''post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})  '''


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})   

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk) 

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if user.get_username == post.author:
        post.delete()
    return redirect('post_list')   

'''def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
'''
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
