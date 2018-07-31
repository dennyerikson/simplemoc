from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', 'simplemoc.core.views.home', name='home'),
    url(r'^contato/$', 'simplemoc.core.views.contact', name='contact'),
]