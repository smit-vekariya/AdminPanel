
from django.urls import path
from . import views

app_name="apiapp"

urlpatterns = [
    path('get_movies/',views.get_movies,name="get_movies"),
    path('movie_details/',views.movie_details,name="movie_details"),
    path('home_details/',views.home_details,name="home_details"),
]
