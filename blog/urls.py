from django.urls import path
from blog.views import (
    about_controller,
    post_create_controller,
    post_detail_controller,
    post_delete_controller,
    post_list_controller,
    user_post_list_controller,
    post_update_controller,
    post_comment_controller,
    category_controller,


)

urlpatterns = [
    path('', post_list_controller.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', user_post_list_controller.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', post_detail_controller.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', post_create_controller.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', post_update_controller.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', post_delete_controller.PostDeleteView.as_view(), name='post-delete'),
    path('about/', about_controller.about, name='blog-about'),
    path('post/<int:pk>/comment', post_comment_controller.PostCommentView.as_view(), name='post-comment'),
    path('category/<str:cats>', category_controller.CategoryView, name='category'),


]
