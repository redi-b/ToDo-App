from django.urls import path
from . import views

urlpatterns = [
    path("/", views.index, name="index"),
    path("add_todo/", views.add_todo, name="add_todo"),
    path('delete/delete_all/', views.delete_all, name="delete_all"),
    path('delete/delete_item/<int:todo_id>', views.delete_item, name="delete_item"),
    path('delete/delete_completed/', views.delete_completed, name="delete_completed"),
    path('delete/delete_due/', views.delete_due, name="delete_due"),
    path("search/", views.search, name="search"),
    path("done/done_item/<int:todo_id>", views.done_item, name="done_item"),
    path("done/done_all/", views.done_all, name="done_all")
]
