from django.conf.urls import url, include
import simplemoc

urlpatterns = [
    # url(r'^$', 'simplemoc.core.views.home', name='home'),
    url(r'^$', simplemoc.core.views.home, name='home'),
    url(r'^contato/$', simplemoc.core.views.contact, name='contact'),
    # url(r'^contato/$', 'simplemoc.core.views.contact', name='contact'),
]