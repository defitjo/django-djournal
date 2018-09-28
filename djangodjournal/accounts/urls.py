from django.urls import path, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
  re_path(r'^signup/$', views.signup_path, name="signup"),
  re_path('^login/$', views.login_path, name="login"),
  re_path('^logout/$', views.logout_path, name="logout"),
]