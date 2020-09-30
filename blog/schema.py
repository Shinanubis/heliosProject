# blog/schema.py
import graphene
from graphene import ObjectType, Mutation, String, Int
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
    all_articles = graphene.List(ArticleType)
    article = graphene.Field(ArticleType, id=graphene.Int())
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, name=graphene.String())
    all_comments = graphene.List(CommentType)
    comment = graphene.Field(CommentType, author=graphene.String())
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, username=graphene.String())

    def resolve_all_articles(self, info, **kwargs):
        return Article.objects.all()

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_article(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Article.objects.get(id=id)


    def resolve_category(self, info, **kwargs):
        name = kwargs.get("name")
        if name is not None:
            return Category.objects.get(name=name)

    def resolve_comment(self, info, **kwargs):
        author = kwargs.get("author")
        if author is not None:
            return Comment.objects.get(author=author)

    def resolve_user(self, info, **kwargs):
        username = kwargs.get("username")
        if username is not None:
            return User.objects.get(username=username)




class CreateCategory(Mutation):
    id = Int()
    name = String()

    class Arguments:
        id = Int()
        name = String()


    def mutate(root, info, name, ):
        category = Category(name=name)
        category.save()

        return CreateCategory(
            id=category.id,
            name=category.name
        )



class CreateComment(Mutation):
    id = Int()
    user_username = String()
    content = String()
    related_paper_title = String()

    class Arguments:
        id = Int()
        user_username = Int()
        content = String()
        related_paper_title = Int()


    def mutate(root, info, user_username, content, related_paper_title):
        comment = Comment(author=User.objects.get(pk=user_username), content=content, related_paper=Article.objects.get(pk=related_paper_title))
        comment.save()

        return CreateComment(
            id=comment.id,
            user_username=comment.author,
            content=comment.content,
            related_paper_title=comment.related_paper
        )


class Mutation(ObjectType):
    create_category = CreateCategory.Field()
    create_comment = CreateComment.Field()