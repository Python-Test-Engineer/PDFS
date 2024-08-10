from django.urls import path

from . import views

app = "studybuddy"

urlpatterns = [
    path("", views.home, name="home"),
]
