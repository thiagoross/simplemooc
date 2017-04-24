from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('simplemooc.core.urls')),
    url(r'^contato/$', 'simplemooc.core.views.contact', name='contact'),
)