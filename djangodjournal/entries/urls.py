from django.urls import path, re_path
from . import views

app_name = 'entries'

urlpatterns = [
    path('', views.entries_list, name="list"),
    path('/new/', views.entry_new, name="new"),
    path('/<slug:slug>/', views.entry_details, name="details"),
]