from django.conf.urls import url

from . import views
#app_name = 'activelist'
urlpatterns = [
    url(r'^$', views.login, name = 'login'),
    url(r'^index',views.index, name = 'index'),
    url(r'^add',views.add_active, name = 'add_active'),
    url(r'^edit/(\d+)',views.edit_active, name = 'edit_active'),
    url(r'^delete/(\d+)',views.delete_active, name = 'delete_active'),
    url(r'^logout/',views.logout, name = 'logout')
]
