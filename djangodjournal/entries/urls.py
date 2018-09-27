from django.urls import path, re_path
from . import views

app_name = 'entries'

urlpatterns = [
    re_path(r'^$', views.entries_list, name="list"),
    re_path('(?P<slug>[\w-]+)/$', views.entry_details, name="details"),
]