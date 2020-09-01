from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
  return render(request, 'blogs/index.html')

@login_required
def blog(request):
  posts = BlogPost.objects.filter(owner=request.user).order_by("-date_added")
  context = {'posts': posts}
  return render(request, 'blogs/blog.html', context)

@login_required
def post(request, post_id):
  post = BlogPost.objects.get(id=post_id)
  if check_post_owner(request, post):
    raise Http404
  context = {'post': post}
  return render(request, 'blogs/post.html', context)

@login_required
def delete_post(request, post_id):
  post = BlogPost.objects.get(id=post_id)
  if check_post_owner(request, post):
    raise Http404
  post.delete()
  return redirect('blogs:blog')

@login_required
def edit_post(request, post_id):
  post = BlogPost.objects.get(id=post_id)
  if check_post_owner(request, post):
    raise Http404
  if request.method != 'POST':
    form = BlogPostForm(instance=post)
  else:
    form = BlogPostForm(instance=post, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('blogs:blog')
  
  context = {'form': form, 'post': post}
  return render(request,'blogs/edit_post.html', context)

@login_required
def new_post(request):
  if request.method != 'POST':
    form = BlogPostForm()
  else:
    form = BlogPostForm(request.POST)
    if form.is_valid():
      new_post = form.save(commit=False)
      new_post.owner = request.user
      new_post.save()
    return redirect('blogs:blog')

  context = {'form': form}
  return render(request, 'blogs/new_post.html', context)

def check_post_owner(request, post):
  return request.user != post.owner

  