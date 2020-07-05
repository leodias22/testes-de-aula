from django.urls import path

from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("leo", views.leo, name="leo"),
    path("<str:name>", views.greet, name="greet")
]