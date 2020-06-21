from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_todo/", views.add_todo, name="add_todo"),
    path("delete_item/<int:todo_id>", views.delete_item, name="delete_item"),
    path("delete_all/", views.delete_all, name="delete_all"),
    path("search/", views.search, name="search")
]
