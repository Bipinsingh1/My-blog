from django.views.generic import ListView
from blog.models import Post, Category


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        latest_post = Post.objects.all().order_by('-date_posted')[0:3]
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["latest_post"] = latest_post
        context['cat_list'] = cat_list
        return context
