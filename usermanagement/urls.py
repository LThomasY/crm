from django.conf.urls import url

from . import views
#app_name = 'statement'
urlpatterns = [
    url(r'^$', views.user, name='user'),
    url(r'^add_user/$', views.add_user, name='add_user'),
    url(r'^change_acount_type/(.+)/$', views.change_acount_type, name='change_acount_type'),
    url(r'^reset_password/(.+)/$', views.reset_password, name='reset_password'),
    url(r'^delete_user/(.+)/$', views.delete_user, name='delete_user'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^delete_project/(.+)/$', views.delete_project, name='delete_project'),
    url(r'^add_client/$', views.add_client, name='add_client'),
    url(r'^delete_client/(.+)/$', views.delete_client, name='delete_client'),
]
