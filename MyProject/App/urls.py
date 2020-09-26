from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('Blogs/',views.blog, name = 'blog'),
    path('accounts/', include('django.contrib.auth.urls')),
]