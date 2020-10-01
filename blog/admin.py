# blog/admin.py
from django.contrib import admin
from blog.models import Article, Category, Comment


@admin.register(Article, Category, Comment)


class ArticleAdmin(admin.ModelAdmin):
    #Admin for the blog post.
    pass
