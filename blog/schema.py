# blog/schema.py

import graphene
from graphene_django import DjangoObjectType
from blog.models import Article


class ArticleType(DjangoObjectType):
    """Defines a graphql type for our article."""
    class Meta:
        model = Article
        filter_fields = ['author', 'title', 'category']


class Query(graphene.ObjectType):
    """Create the main query interface."""
    articles = graphene.List(ArticleType)

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()
