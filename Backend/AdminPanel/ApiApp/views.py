import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ApiApp.models import MovieInfo

# Create your views here.


@csrf_exempt
def get_movies(request):
     movies = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type","duration","description","language","genres","cast","published")
     movies_info = {"data":[]}
     for data in movies:
          movies_info["data"].append({
               "id":data["id"],
               "name":data["name"],
               "slug":data["slug"],
               "release_date":str(data["release_date"]),
               "trailer_url":data["trailer_url"],
               "download_url":data["download_url"],
               "thumbnail_url":data["thumbnail_url"],
               "source_url":data["source_url"],
               "screenshots":data["screenshots"],
               "source_type":data["source_type"],
               "duration":data["duration"],
               "description":data["description"],
               "language":str(data["language"]),
               "genres":data["genres"],
               "cast":data["cast"],
          })

     return HttpResponse(json.dumps(movies_info))


@csrf_exempt
def movie_details(request):
     movie_id = request.POST.get("movie_id")
     movies = MovieInfo.objects.filter(id=movie_id).values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type","duration","description","language","genres","cast","published")
     movies_info = {"data":[]}
     for data in movies:
          movies_info["data"].append({
               "id":data["id"],
               "name":data["name"],
               "slug":data["slug"],
               "release_date":str(data["release_date"]),
               "trailer_url":data["trailer_url"],
               "download_url":data["download_url"],
               "thumbnail_url":data["thumbnail_url"],
               "source_url":data["source_url"],
               "screenshots":data["screenshots"],
               "source_type":data["source_type"],
               "duration":data["duration"],
               "description":data["description"],
               "language":str(data["language"]),
               "genres":data["genres"],
               "cast":data["cast"],
          })

     return HttpResponse(json.dumps(movies_info))


@csrf_exempt
def home_details(request):
     movies = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type","duration","description","language","genres","cast","published").order_by('-release_date')[:3]
     source_data = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type","duration","description","language","genres","cast","published")
     movies_info ={"data": [{
               "section_name": "Banner",
               "data": []
          },
          {
               "section_name": "NetFlix",
               "data": []
          },
          {
               "section_name": "Amazon",
               "data": []
          },
          {
               "section_name": "Disney",
               "data": []
          }]}
     for data in movies:
        movies_info["data"][0]["data"].append({
               "id":data["id"],
               "name":data["name"],
               "slug":data["slug"],
               "release_date":str(data["release_date"]),
               "trailer_url":data["trailer_url"],
               "download_url":data["download_url"],
               "thumbnail_url":data["thumbnail_url"],
               "source_url":data["source_url"],
               "screenshots":data["screenshots"],
               "source_type":data["source_type"],
               "duration":data["duration"],
               "description":data["description"],
               "language":str(data["language"]),
               "genres":data["genres"],
               "cast":data["cast"],
          })

     for data in source_data:
          if data["source_type"]=="NetFlix":
               index = 1
          elif data["source_type"]=="Amazon":
               index = 2
          elif data["source_type"]=="Disney":
               index = 3
          else:
               break
          movies_info["data"][index]["data"].append({
               "id":data["id"],
               "name":data["name"],
               "slug":data["slug"],
               "release_date":str(data["release_date"]),
               "trailer_url":data["trailer_url"],
               "download_url":data["download_url"],
               "thumbnail_url":data["thumbnail_url"],
               "source_url":data["source_url"],
               "screenshots":data["screenshots"],
               "source_type":data["source_type"],
               "duration":data["duration"],
               "description":data["description"],
               "language":str(data["language"]),
               "genres":data["genres"],
               "cast":data["cast"],
          })

     return HttpResponse(json.dumps(movies_info))