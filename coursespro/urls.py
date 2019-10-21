from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Examples:
    # url(r'^$', 'coursespro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'), in),

    path('api/', include('courses.urls')),
    path('users/', include('accounts.urls')),
    #url('api-auth/', include('rest_framework.urls')),
    url('admin/', admin.site.urls),
]
