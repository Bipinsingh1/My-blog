from django import forms
from blog.models import Post


class PostUpdate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'image', 'content')
