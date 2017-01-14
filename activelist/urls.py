from django.conf.urls import url

from . import views
#app_name = 'activelist'
urlpatterns = [
    url(r'^$', views.login, name = 'login'),
    url(r'^index',views.index, name = 'index'),
    url(r'^add',views.add_active, name = 'add_active'),
    url(r'^edit/(.+)',views.edit_active, name = 'edit_active'),
]
