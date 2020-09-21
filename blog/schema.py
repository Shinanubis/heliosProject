# blog/schema.py

import graphene
from graphene_django import DjangoObjectType
from blog.models import Article
from blog.models import Category
from blog.models import Comment


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


class Query(graphene.ObjectType):
    """Create the main query interface."""
    articles = graphene.List(ArticleType)
    categories = graphene.List(CategoryType)
    comments = graphene.List(CommentType)

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()
