from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
	return render(request,'index.html')


# Blogs View
def blog(request):
	return render(request,'blogs.html')


def register(request):
    form = UserCreationForm
    return render(request, 'register.html', {'form':form})