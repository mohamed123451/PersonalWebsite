from django.urls import path
from . import views

appname = 'blog'

urlpatterns = [
    path ('', views.allBlogs, name="allblogs")
]