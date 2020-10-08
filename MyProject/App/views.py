from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import *


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


# Create your views here.


def index(request):
	return render(request,'index.html')


# Blogs View
def blog(request):
	return render(request,'blogs.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


class PostListView(ListView):
    model = Post
    template_name = 'index.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']


class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  



class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'  
    fields = ['cover_image','title', 'content']


    def form_valid(self, form):
        
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['cover_image','title', 'content']

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def Events(request):
    return render(request, 'events.html')

            
@login_required
def profile(request):
    if request.method =='POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, "Your account been updated!")
            return redirect('profile')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
   
    context = {
        'p_form':p_form,
        'u_form':u_form,
    }   
    return render(request, 'profile.html', context)

