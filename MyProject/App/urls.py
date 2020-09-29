from django.urls import path, include
from .views import (
    PostListView,
    # PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    createPost,
)
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("post/", createPost, name="post"),
    path("", PostListView.as_view(), name="index"),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path("post/<int:pk>/", views.post_detail, name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
