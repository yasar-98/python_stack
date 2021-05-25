from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/create', views.create),
    path('shows/new', views.new),
    path('shows/<int:num>', views.nums),
    path('shows/<int:num>/edit', views.edit),
    path('h/<int:num>', views.update),
    path('shows/<int:num>/destroy', views.destroy),
]