from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100, default="Hello my new blog post")
    category = models.CharField(max_length=100, blank=True)
    content = HTMLField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='post_pics')

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
