from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/new/', PostCreateView.as_view(), name='new'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
   
]