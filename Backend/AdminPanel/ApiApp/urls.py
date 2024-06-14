
from django.urls import path
from . import views
from ApiApp.views import *

from Account.manager import check_secret_key


def path_with_key(regex, view, kwargs=None, name=None):
    return path(regex, check_secret_key(view), kwargs, name)

app_name="apiapp"

urlpatterns = [
    # path('',views.welcome,name="welcome"),
    path('',Welcome.as_view(),name="welcome"),

    #ios
    # path_with_key('movie_details/',views.movie_details,name="movie_details"),
    path('movie_details/',views.movie_details,name="movie_details"),
    path('movie_details2/',MovieDetails.as_view(),name="movie_details"),
    path('movie_details3/<int:pk>/',MovieDetails2.as_view(),name="movie_details"),
    # path_with_key('home_details/',views.home_details,name="home_details"),
    path('home_details/',views.home_details,name="home_details"),
    path('home_details2/',HomeDetails.as_view({'get': 'list'}),name="home_details"),
    path('movie_search/',views.movie_search,name="movie_search"),
    path('movie_search2/',MovieSearch.as_view({'get': 'list'}),name="movie_search"),
    path_with_key('download_link/',views.download_link,name="download_link"),

    #collect data
    path('movie_scheduler/',views.movie_scheduler,name="movie_scheduler"),
    path('web_scheduler/',views.web_scheduler,name="web_scheduler"),
    path('data_transfer/',views.data_transfer,name="data_transfer"),
    path('data_transfer2/',DataTransfer.as_view(),name="data_transfer"),
    path('data_retrieve/',views.data_retrieve,name="data_retrieve"),
    path('data_retrieve2/',DataRetrieve.as_view(),name="data_retrieve"),
    path('download_csv/',views.download_csv,name="download_csv"),
    path('download_csv2/',DownloadCSV.as_view(),name="download_csv"),
    path('csv_to_modal/',views.csv_to_modal,name="csv_to_modal"),
    path('csv_to_modal2/',CsvToModal.as_view(),name="csv_to_modal"),
    path('app_info/',views.app_info,name="app_info"),
    path('app_info2/',AppInfoView.as_view({'get': 'list'}),name="app_info"),

    path('insert_movie/',InsertMovie.as_view(), name="insert_movie")
]
