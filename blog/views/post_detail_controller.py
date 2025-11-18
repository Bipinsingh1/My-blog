from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post, Category, Comment
from blog.forms.CommentForm import CommentForm


class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        latest_post = Post.objects.all().order_by('-date_posted')[0:3]
        content = super(PostDetailView, self).get_context_data(*args, **kwargs)
        content['latest_post'] = latest_post
        content['cat_list'] = cat_list
        content['comment_form'] = CommentForm()
        return content
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return HttpResponseRedirect(reverse('post-detail', kwargs={'pk': self.object.pk}))
        
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)

