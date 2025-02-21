from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("todos/", views.todos, name= "Todos"),
    path("todos/detalles/<int:id>", views.detalles, name="detalles"),
    path("testeo/", views.testeo, name = 'testeo'),
    path('visualiq/', views.visualiq, name = 'visualiq'),
]