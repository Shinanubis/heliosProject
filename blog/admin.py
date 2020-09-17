# blog/admin.py
from django.contrib import admin
from blog.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin for the blog post."""
    pass
