"""heliosProject URL Configuration"""


from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="application.html"), name="app"),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]
