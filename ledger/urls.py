from django.conf.urls import url

from . import views

app_name = 'ledger'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^/add_user_page/$', views.add_user_page, name='add_user_page'),
    url(r'^/add_user/$', views.add_user, name='add_user'),
    url(r'^(?P<pk>[0-9]+)/user_detail/$', views.UserDetailView.as_view(), name='detail'),
]
