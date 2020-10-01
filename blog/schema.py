# blog/schema.py
import graphene
from graphene import ObjectType, Mutation, String, Int
from graphene_django import DjangoObjectType

from blog.models import Article
from blog.models import Category
from blog.models import Comment
from django.contrib.auth.models import User

#Defines a graphql type for our article.
class ArticleType(DjangoObjectType):

    class Meta:
        model = Article

#Defines a graphql type for our category.
class CategoryType(DjangoObjectType):

    class Meta:
        model = Category

#Defines a graphql type for our comment.
class CommentType(DjangoObjectType):

    class Meta:
        model = Comment

#Defines a graphql type for our user.
class UserType(DjangoObjectType):

    class Meta:
        model = User


class Query(graphene.ObjectType):
    #Create the main query interface.
    all_articles = graphene.List(ArticleType)
    article = graphene.Field(ArticleType, id=graphene.Int())
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, name=graphene.String())
    all_comments = graphene.List(CommentType)
    comment = graphene.Field(CommentType, author=graphene.String())
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, username=graphene.String())

    #Get all article object
    def resolve_all_articles(self, info, **kwargs):
        return Article.objects.all()

    #Get all category object
    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    #Get all comment object
    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    #Get all user object
    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    #Retrieve article object by id
    def resolve_article(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Article.objects.get(id=id)

    #Retrieve category object by name
    def resolve_category(self, info, **kwargs):
        name = kwargs.get("name")
        if name is not None:
            return Category.objects.get(name=name)

    #Retrieve comment object by author
    def resolve_comment(self, info, **kwargs):
        author = kwargs.get("author")
        if author is not None:
            return Comment.objects.get(author=author)

    #Retrieve user object by username
    def resolve_user(self, info, **kwargs):
        username = kwargs.get("username")
        if username is not None:
            return User.objects.get(username=username)



#Category mutation
class CreateCategory(Mutation):
    id = Int()
    name = String()

    class Arguments:
        id = Int(required=True)
        name = String(required=True)


    def mutate(root, info, name, ):
        category = Category(
            name=name
        )
        category.save()

        return CreateCategory(
            id=category.id,
            name=category.name
        )


#Comment mutation
class CreateComment(Mutation):
    id = Int()
    user_username = String()
    content = String()
    related_paper_title = String()

    class Arguments:
        id = Int(required=True)
        user_username = Int(required=True)
        content = String(required=True)
        related_paper_title = Int(required=True)


    def mutate(root, info, user_username, content, related_paper_title):
        comment = Comment(
            author=User.objects.get(pk=user_username),
            content=content,
            related_paper=Article.objects.get(pk=related_paper_title)
        )
        comment.save()

        return CreateComment(
            id=comment.id,
            user_username=comment.author,
            content=comment.content,
            related_paper_title=comment.related_paper
        )
#Article mutation
class CreateArticle(Mutation):
    id = Int()
    title = String()
    user_username = String()
    content = String()
    comment_id = Int()
    category_name = String()

    class Arguments:
        id = Int(required=True)
        title = String(required=True)
        user_username = Int(required=True)
        content = String(required=True)
        category_name = Int(required=True)


    def mutate(root, info, title,user_username, content, category_name):
        article = Article(
            title=title,
            author=User.objects.get(pk=user_username),
            content=content,
            category=Category.objects.get(pk=category_name)
        )
        article.save()

        return CreateArticle(
            id=article.id,
            user_username=article.author,
            content=article.content,
            category_name=article.category
        )

#User mutation
class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

#Instantiate mutation object
class Mutation(ObjectType):
    create_category = CreateCategory.Field(),
    create_comment = CreateComment.Field(),
    create_article = CreateArticle.Field()
    create_user = CreateUser.Field()