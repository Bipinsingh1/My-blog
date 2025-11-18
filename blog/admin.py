from django.contrib import admin
from blog.models import Post, Comment, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_tag', 'category',  'date_posted')
    search_fields = ['title', 'content', 'category']
    prepopulated_fields = {'title_tag': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)

