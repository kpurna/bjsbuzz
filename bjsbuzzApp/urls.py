from django.conf.urls import patterns, include, url
from django.conf.urls import *
from tastypie.api import Api
from bjsbuzzApp.views import user_details,index
from bjsbuzzApp.api.users import UsersResource, UsersCommentsResource

v1_api = Api(api_name='v1')
v1_api.register(UsersResource())
v1_api.register(UsersCommentsResource())

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', index.index),
    # Examples:
    # url(r'^$', 'bjsbuzz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'', include(v1_api.urls)),
    url(r'^v0/user-details/$',user_details.user_details),
    url(r'^v0/users-comments/$',user_details.userscomments_details),
)
