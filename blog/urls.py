from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.home, name="home"),
    path("blogs", views.blogs, name="blogs"),
    path("blogDetail/<int:id>", views.blogDetail, name="blogDetail"),
]
