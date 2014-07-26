from django.conf.urls import url

from switches import views

urlpatterns = [
    # ex: /switches/
    
    # ex: /switches/5/
    url(r'^(?P<switch_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /switches/active/5/
    url(r'^active/(?P<switch_id>[0-9]+)/$', views.active, name='active'),
    url(r'^$', views.index, name='index')

]
