from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from blog.models import Post
from blog.forms.PostForm import PostForm


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
