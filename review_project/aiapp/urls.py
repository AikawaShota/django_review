from django.urls import path
from . import views


app_name = "aiapp"


urlpatterns = [
    path("index", views.index, name="index"),
]
