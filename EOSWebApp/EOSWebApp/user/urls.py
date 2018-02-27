from django.conf.urls import url

from EOSWebApp.user import views

app_name = 'user'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    ]