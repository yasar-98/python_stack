from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login),
    path('wall', views.wall),
    path('commenting/<int:num>', views.commenting),
    path('posting', views.posting),
    path('deletecom/<int:num>', views.deletecom),
    path('deletepos', views.deletepos),
]
