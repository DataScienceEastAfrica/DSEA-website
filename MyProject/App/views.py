from django.shortcuts import render, redirect  
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def index(request):
	return render(request,'index.html')


# Blogs View
def blog(request):
	return render(request,'blogs.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
