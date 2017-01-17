from django.conf.urls import url

from . import views
#app_name = 'statement'
urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^search',views.search, name = 'search'),
#    url(r'^add',views.add_active, name = 'add_active'),
#    url(r'^edit/(\d+)',views.edit_active, name = 'edit_active'),
]
