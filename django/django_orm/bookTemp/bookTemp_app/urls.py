from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
    path('book', views.book),	   
    path('book/<int:num>', views.books),	   
    path('booking/<int:num>', views.booking),
    path('author', views.index2),	   
    path('authorg', views.authorg),
    path('author/<int:num>', views.authors),	   
    path('authoring/<int:num>', views.authoring),
]