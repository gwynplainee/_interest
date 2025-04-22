from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'core'

urlpatterns = [
    path('posts/', views.PostView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostView.as_view(), name='post_detail'),
    path('posts/list/', views.post_list, name='post_list_all'),
    path('comments/create/', views.comment_create, name='comment_create'),
    path('posts/<int:post_id>/comments/', views.comment_list, name='comment_list'),
    path('posts/<int:post_id>/like/', views.like_toggle, name='like_toggle'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
    path('follow/', views.follow_toggle, name='follow_toggle'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('liked_posts/', views.liked_posts, name='liked_posts'),
    path('followed_posts/', views.followed_posts, name='followed_posts'),
    path('search/', include('search.urls')),  # Move search here
]