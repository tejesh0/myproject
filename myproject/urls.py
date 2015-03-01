from django.conf.urls import patterns, include, url
from django.contrib import admin
from myproject import views 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^blog/', include('blog.urls')),
    url(r'^', views.home ),
)
