from blog.models import Post
from django.shortcuts import render


def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('_', '')).order_by('-date_posted')
    return render(request, 'blog/categories.html',
                  {'cats': cats.title().replace('_', ''), 'category_post': category_post})
