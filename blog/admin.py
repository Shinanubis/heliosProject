# blog/admin.py
from django.contrib import admin
from blog.models import Article
from blog.models import Category
from blog.models import Comment

@admin.register(Article)
@admin.register(Category)
@admin.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    """Admin for the blog post."""
    pass
