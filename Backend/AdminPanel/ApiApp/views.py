import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ApiApp.models import MovieInfo, CyberUser, SourceType
from Account import manager
import time
import requests
from django.conf import settings
# Create your views here.

def welcome(request):
     try:
          return render(request, template_name="ApiApp/welcome.html")
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({str(e)}))


@csrf_exempt
def movie_details(request):
     try:
          movie_id = json.loads(request.body)["movie_id"]
          movies = MovieInfo.objects.filter(id=movie_id).values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published")
          movies_info = {"data":{}, "status": 1, "message": "success"}
          for data in movies:
               movies_info["data"].update({
                    "id":data["id"],
                    "name":data["name"],
                    "slug":data["slug"],
                    "release_date":str(data["release_date"]),
                    "trailer_url":data["trailer_url"],
                    "download_url":data["download_url"],
                    "thumbnail_url":data["thumbnail_url"],
                    "source_url":data["source_url"],
                    "screenshots":data["screenshots"],
                    "source_type":data["source_type__name"],
                    "duration":data["duration"],
                    "description":data["description"],
                    "language":str(data["language"]),
                    "genres":data["genres"],
                    "cast":data["cast"],
               })
          return HttpResponse(json.dumps(movies_info))
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":{}, "status": 0, "message": str(e)}))



@csrf_exempt
def home_details(request):
     try:
          movies = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published","file_id").order_by('-release_date')[:3]
          source_data = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published","file_id")
          data_ = []
          source_type = SourceType.objects.values("name")
          data_.append({"section_name": "Banner", "data": []})
          for ott in source_type:
               data_.append({"section_name": ott["name"],"data": []})
          for data in source_data:
               for ot in data_:
                    if ot["section_name"] == data["source_type__name"]:
                         ot["data"].append({
                              "id":data["id"],
                              "name":data["name"],
                              "slug":data["slug"],
                              "release_date":str(data["release_date"]),
                              "trailer_url":data["trailer_url"],
                              "download_url":data["download_url"],
                              "thumbnail_url":data["thumbnail_url"],
                              "source_url":data["source_url"],
                              "screenshots":data["screenshots"],
                              "source_type":data["source_type__name"],
                              "duration":data["duration"],
                              "description":data["description"],
                              "language":str(data["language"]),
                              "genres":data["genres"],
                              "cast":data["cast"],
                         })
          for data in movies:
               data_[0]["data"].append({
                    "id":data["id"],
                    "name":data["name"],
                    "slug":data["slug"],
                    "release_date":str(data["release_date"]),
                    "trailer_url":data["trailer_url"],
                    "download_url":data["download_url"],
                    "thumbnail_url":data["thumbnail_url"],
                    "source_url":data["source_url"],
                    "screenshots":data["screenshots"],
                    "source_type":data["source_type__name"],
                    "duration":data["duration"],
                    "description":data["description"],
                    "language":str(data["language"]),
                    "genres":data["genres"],
                    "cast":data["cast"],
               })
          data_ = [ot for ot in data_ if len(ot["data"]) != 0]
          movies_info = {"data": data_,"status": 1, "message":"success"}
          return HttpResponse(json.dumps(movies_info))
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))


@csrf_exempt
def movie_search(request):
     try:
          search_data = json.loads(request.body)["search_data"]
          movies = MovieInfo.objects.filter(name__icontains=search_data).values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published").order_by('-release_date')[:3]
          if len(movies) == 0:
               movies = MovieInfo.objects.filter(source_type__name__icontains=search_data).values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published").order_by('-release_date')[:3]
          movies_info = {"data":[], "status": 1, "message": "success"}
          if len(movies) != 0:
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
                         "source_type":data["source_type__name"],
                         "duration":data["duration"],
                         "description":data["description"],
                         "language":str(data["language"]),
                         "genres":data["genres"],
                         "cast":data["cast"],

                    })
               return HttpResponse(json.dumps(movies_info))
          elif len(movies) == 0 and search_data =="":
               movies = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published","file_id").order_by('-release_date')[:10]
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
                         "source_type":data["source_type__name"],
                         "duration":data["duration"],
                         "description":data["description"],
                         "language":str(data["language"]),
                         "genres":data["genres"],
                         "cast":data["cast"],
                    })
               return HttpResponse(json.dumps(movies_info))
          else:
               return HttpResponse(json.dumps({"data":[], "status": 1, "message": "success"}))
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))


@csrf_exempt
def download_link(request):
     try:
          movie_id = json.loads(request.body)["movie_id"]
          if movie_id:
               movie_details = MovieInfo.objects.filter(id=movie_id).values("upload_by__username","upload_by__password","file_id").first()
               if movie_details:
                    username = movie_details["upload_by__username"]
                    password = movie_details["upload_by__password"]
                    file_id = movie_details["file_id"]
                    token_and_id = json.loads(get_access_token(username, password))
                    account_id = token_and_id["account_id"]
                    access_token = token_and_id["access_token"]
                    download_url = f"{settings.CYBER_FILE}/file//download?access_token={access_token}&account_id={account_id}&file_id={file_id}"
                    response = requests.request("GET", download_url).json()
                    download_url = response["data"]["download_url"]
                    return HttpResponse(json.dumps({"data":{"download_url":download_url}, "status": 1, "message": "success"}))
               else:
                    return HttpResponse(json.dumps({"data":{}, "status": 1, "message": "Movie not found"}))
          return HttpResponse(json.dumps({"data":{}, "status": 1, "message": "Movie id not found"}))
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":{}, "status": 0, "message": str(e)}))


@csrf_exempt
def movie_scheduler(request):
     try:
          data = json.loads(request.body)
          username = data["username"]
          password = data["password"]
          if username and password:
               token_and_id = json.loads(get_access_token(username, password))
               access_token = token_and_id["access_token"]
               account_id = token_and_id["account_id"]
               url = f"{settings.CYBER_FILE}/folder/listing?access_token={access_token}&account_id={account_id}"
               response = requests.request("GET", url).json()
               file_ids = MovieInfo.objects.filter(upload_by__username=username).values("file_id")
               file_ids =[id["file_id"] for id in file_ids]
               for data in response["data"]["files"]:
                    if data["id"] not in file_ids:
                         name = data["filename"].split("(")[0]
                         year = data["filename"].split("(")[1].split(")")[0]

               return HttpResponse(json.dumps({"data":[response], "status": 1, "message": "Movie fetch successfully."}))
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))


@csrf_exempt
def authorize(request):
     try:
          data =  json.loads(request.body)
          username = data["username"]
          password = data["password"]
          if username and password:
               token_and_id = json.loads(get_access_token(username, password))
               account_id = token_and_id["account_id"]
               access_token = token_and_id["access_token"]
               CyberUser.objects.filter(account_id=account_id).update(cyber_access_token=access_token)
               return HttpResponse(json.dumps({"data":[{"access_token":access_token}], "status": 1, "message": "Authentication successfully."}))
          else:
               return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Username or password Required"}))
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))



def get_access_token(username,password):
     try:
          url = f"{settings.CYBER_FILE}/authorize?username={username}&password={password}"
          response = requests.request("GET", url).json()
          account_id = response["data"]["account_id"]
          access_token = response["data"]["access_token"]
          return json.dumps({"access_token":access_token,"account_id":account_id})
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))
