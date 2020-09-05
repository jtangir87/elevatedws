from django.contrib import admin
from .models import BlogCategory, BlogPost

# Register your models here.


class BlogModelAdmin(admin.ModelAdmin):
    fields = ('title', 'categories', 'page_css', 'header_img',
              'slug', 'post', 'page_js', 'published')


admin.site.register(BlogCategory)
admin.site.register(BlogPost)
