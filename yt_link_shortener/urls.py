from django.urls import path

from . import views

urlpatterns = [
    path('', views.link_shortener, name='link_shortener'),
]
