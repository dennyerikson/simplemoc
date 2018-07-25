from django.conf.urls import url, include, patterns

urlpatterns = patterns ('simplemoc.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)