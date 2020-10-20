from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    Events,
    profile,
    likeView,
    PostCreateView,
    PostComment,
    
)
from . import views 

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    
    path('',PostListView.as_view(), name = 'index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', PostComment.as_view(), name='post-comment'),
    path('profile/', profile,name='profile'),
    path('events/', Events, name='Events'),
    path('like/<int:pk>/', likeView, name='like_post'),

]
