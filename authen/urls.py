from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views



urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('password-reset', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), 
        name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), 
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), 
        name='password_reset_complete'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
]
