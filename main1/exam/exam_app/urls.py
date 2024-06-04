from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
