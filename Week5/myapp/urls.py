from django.urls import path
from .views import indexPage

urlpatterns = [
    path("", indexPage, name="home"),
]