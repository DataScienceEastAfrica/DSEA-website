from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    Events,
    profile,
    
)
from . import views 

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    
    path('',PostListView.as_view(), name = 'index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/', profile,name='profile'),
    path('events/', Events, name='Events')

]
