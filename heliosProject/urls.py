"""heliosProject URL Configuration"""


from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="application.html"), name="app"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    re_path('^.*$', TemplateView.as_view(template_name="application.html")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



