from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pipelineapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','core.views.index'),
)

#http://stackoverflow.com/questions/12800862
#static files don't work for gunicorn in development without this:
urlpatterns += staticfiles_urlpatterns();
