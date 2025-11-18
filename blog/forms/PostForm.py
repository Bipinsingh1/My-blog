from django import forms
from blog.models import Post, Category

def get_categories():
    # This will be called when the form is created, not at import time
    choices = [('', 'Select a category')]  # Add an empty default option
    try:
        # Get all categories and format them as tuples of (name, name)
        categories = Category.objects.all()
        if categories.exists():
            category_choices = [(cat.name, cat.name) for cat in categories]
            return choices + category_choices
        else:
            # If no categories exist, add a default one
            return choices + [('Uncategorized', 'Uncategorized')]
    except Exception:
        # If there's any error, provide a fallback
        return choices + [('Uncategorized', 'Uncategorized')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'image', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # This gets choices at form initialization time, not import time
        self.fields['category'].widget.choices = get_categories()
