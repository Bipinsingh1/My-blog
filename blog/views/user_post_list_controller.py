from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView
from blog.models import Post, Category


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        latest_post = Post.objects.all().order_by('-date_posted')[0:3]
        content = super(UserPostListView, self).get_context_data(*args, **kwargs)
        content['latest_post'] = latest_post
        content['cat_list'] = cat_list
        return content

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
