from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('books', views.books),
    path('logout', views.logout),
    path('login', views.login),
    path('booking', views.booking),
    path('add_favourite/<int:num>', views.add_favourite),
    path('books/<int:num>', views.going),
    path('event/<int:num>', views.event),
    path('unfav/<int:num>', views.unfav),
]