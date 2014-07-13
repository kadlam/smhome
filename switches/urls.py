from django.conf.urls import url

from switches import views

urlpatterns = [
    # ex: /switches/
    url(r'^$', views.index, name='index'),
    # ex: /switches/5/
    url(r'^(?P<switch_id>[0-9]+)/$', views.detail, name='detail'),
]