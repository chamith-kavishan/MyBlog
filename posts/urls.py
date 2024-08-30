from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
from .views import post_detail, bookmark_post,bookmarked_posts

urlpatterns = [
    path('', views.post_form, name='post_insert'),
    path('view/<int:id>/', views.post_detail , name='post_detail'),
    path('<int:id>/', views.post_form, name='post_update'),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
    path('list/', views.post_list, name='post_list'),
    path('user_posts/', login_required(views.user_post_list), name='user_post_list'),
    path('bookmark/<int:post_id>/', bookmark_post, name='bookmark_post'),
    path('bookmarked_posts/', bookmarked_posts, name='bookmarked_posts'),
]