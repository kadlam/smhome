from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sprinklers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^switches/', include('switches.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
