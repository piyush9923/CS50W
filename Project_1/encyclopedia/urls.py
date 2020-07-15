from django.urls import path

from . import views

app_name = "wikipedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.info, name='title')
]
