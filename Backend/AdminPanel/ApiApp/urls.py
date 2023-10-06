
from django.urls import path
from . import views

app_name="apiapp"

urlpatterns = [
    path('',views.welcome,name="welcome"),

    #ios
    path('movie_details/',views.movie_details,name="movie_details"),
    path('home_details/',views.home_details,name="home_details"),
    path('movie_search/',views.movie_search,name="movie_search"),
    path('download_link/',views.download_link,name="download_link"),

    #collect data
    path('authorize/',views.authorize,name="authorize"), #temp not use
    path('moive_scheduler/',views.moive_scheduler,name="moive_scheduler"),
]
