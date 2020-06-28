from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from coursespro.schema import schema

urlpatterns = [
    # Examples:
    # url(r'^$', 'coursespro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'), in),

    path('api/', include('courses.urls')),
    path('users/', include('accounts.urls')),
    #url('api-auth/', include('rest_framework.urls')),
    url('admin/', admin.site.urls),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
