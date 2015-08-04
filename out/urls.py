from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('chat.views',
    url(r'^$', 'index'),
    url(r'^chat/$', 'index'),
    url(r'^chat/send/$', 'send'),
    url(r'^chat/post/$', 'post'),
    url(r'^out/$', 'out'),
    # Examples:
    # url(r'^$', 'slack.views.home', name='home'),
    # url(r'^slack/', include('slack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
