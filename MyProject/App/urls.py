<<<<<<< HEAD
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views 

urlpatterns = [
    path('',PostListView.as_view(), name = 'index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

=======
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('Blogs/',views.blog, name = 'blog'),
    path('accounts/', include('django.contrib.auth.urls')),
>>>>>>> d1720999a229cb1cf707980cbf1c1e6550391a50
]