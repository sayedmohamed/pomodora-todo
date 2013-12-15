from django.conf.urls import patterns, include, url
from mytodo.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pomotodo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',main_page,name="main_page"),
    url(r'^user/(\w+)/$',user_page,name="user_page"),
    url(r'^login/$','django.contrib.auth.views.login',name="login"),
    url(r'^logout/$',logout_page,name="logout"),
)
