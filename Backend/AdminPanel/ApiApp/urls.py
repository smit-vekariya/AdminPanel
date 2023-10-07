
from django.urls import path
from . import views

from Account.manager import check_secret_key


def path_with_key(regex, view, kwargs=None, name=None):
    return path(regex, check_secret_key(view), kwargs, name)

app_name="apiapp"

urlpatterns = [
    path('',views.welcome,name="welcome"),

    #ios
    path_with_key('movie_details/',views.movie_details,name="movie_details"),
    path_with_key('home_details/',views.home_details,name="home_details"),
    path('movie_search/',views.movie_search,name="movie_search"),
    path_with_key('download_link/',views.download_link,name="download_link"),

    #collect data
    path('authorize/',views.authorize,name="authorize"), #temp not use
    path('movie_scheduler/',views.movie_scheduler,name="movie_scheduler"),
]
