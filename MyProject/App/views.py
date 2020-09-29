from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import CreatePostForm
from .forms import CommentForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Comment


# Create your views here.


def index(request):
    return render(request, "index.html")


# Blogs View
def blog(request):
    return render(request, "blogs.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("blog")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


class PostListView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


"""Scraped off the CBV for beter implementation of comments
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
"""


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == "POST":
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


class PostCreateView(CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def createPost(request):
    context = {
        "form": CreatePostForm,
    }

    return render(request, "post.html", context)

