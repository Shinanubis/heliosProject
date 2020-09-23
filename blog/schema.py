# blog/schema.py

import graphene
from graphene_django import DjangoObjectType
from blog.models import Article
from blog.models import Category
from blog.models import Comment
from django.contrib.auth.models import User


class ArticleType(DjangoObjectType):
    """Defines a graphql type for our article."""
    class Meta:
        model = Article

class CategoryType(DjangoObjectType):
    """Defines a graphql type for our article."""
    class Meta:
        model = Category

class CommentType(DjangoObjectType):
    """Defines a graphql type for our article."""
    class Meta:
        model = Comment

class UserType(DjangoObjectType):
    """Defines a graphql type for our article."""
    class Meta:
        model = User


class Query(graphene.ObjectType):
    """Create the main query interface."""
    articles = graphene.List(ArticleType)
    categories = graphene.List(CategoryType)
    comments = graphene.List(CommentType)
    users = graphene.List(UserType)

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
