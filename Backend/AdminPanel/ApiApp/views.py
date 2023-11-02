import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ApiApp.models import MovieInfo, CyberUser, SourceType
from Account import manager
import time
import requests
from django.conf import settings
from django.db import transaction
from datetime import datetime
from django.http import JsonResponse
from django.db.models.functions import Cast
from django.db.models import CharField
# Create your views here.
import sys


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
          movies = MovieInfo.objects.filter(id=movie_id).values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published","imdb","size")
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
                    "size":data["size"],
                    "imdb":data["imdb"]
               })
          return HttpResponse(json.dumps(movies_info))
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":{}, "status": 0, "message": str(e)}))


@csrf_exempt
def home_details(request):
     try:
          movies = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published","file_id","size","imdb", "is_web", "season", "episode").order_by('-release_date')[:3]
          source_data = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published","file_id","size","imdb", "is_web", "season", "episode")
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
                              "size":data["size"],
                              "imdb":data["imdb"],
                              "is_web":data["is_web"],
                              "season":data["season"],
                              "episode":data["episode"]
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
                    "size":data["size"],
                    "imdb":data["imdb"],
                    "is_web":data["is_web"],
                    "season":data["season"],
                    "episode":data["episode"]
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
          movies = MovieInfo.objects.filter(name__icontains=search_data).values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published","size","imdb", "is_web", "season", "episode").order_by('-release_date')[:15]
          if len(movies) == 0:
               movies = MovieInfo.objects.filter(source_type__name__icontains=search_data).values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published","size","imdb","is_web", "season", "episode").order_by('-release_date')[:15]
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
                         "size":data["size"],
                         "imdb":data["imdb"],
                         "is_web":data["is_web"],
                         "season":data["season"],
                         "episode":data["episode"]

                    })
               return HttpResponse(json.dumps(movies_info))
          elif len(movies) == 0 and search_data =="":
               movies = MovieInfo.objects.values("id","name","slug","size","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published","file_id", "episode", "season", "is_web", "imdb").order_by('-release_date')[:10]
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
                         "size":data["size"],
                         "imdb":data["imdb"],
                         "is_web":data["is_web"],
                         "season":data["season"],
                         "episode":data["episode"]
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
                    token_and_id = CyberUser.objects.filter(username=username).values("cyber_access_token","account_id").first()
                    account_id = token_and_id["account_id"]
                    access_token = token_and_id["cyber_access_token"]
                    download_url = f"{settings.CYBER_FILE}/file//download?access_token={access_token}&account_id={account_id}&file_id={file_id}"
                    response = requests.request("GET", download_url).json()
                    if response["_status"] == "error":
                         token_and_id = get_access_token(username, password)
                         token_and_id = json.loads(token_and_id)
                         if "msg" in token_and_id:
                              return HttpResponse(json.dumps({"data":[], "status": 1, "message": token_and_id["msg"]}))
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
          with transaction.atomic():
               data = json.loads(request.body)
               username = data["username"]
               password = data["password"]
               if username and password:
                    cyber_user = CyberUser.objects.filter(username=username,is_active=True,is_web_account=False).values("id","source_type_id").first()
                    if cyber_user:
                         token_and_id = get_access_token(username, password)
                         token_and_id = json.loads(token_and_id)
                         if "msg" in token_and_id:
                              return HttpResponse(json.dumps({"data":[], "status": 1, "message": token_and_id["msg"]}))
                         access_token = token_and_id["access_token"]
                         account_id = token_and_id["account_id"]
                         url = f"{settings.CYBER_FILE}/folder/listing?access_token={access_token}&account_id={account_id}"
                         response = requests.request("GET", url).json()
                         file_ids = MovieInfo.objects.filter(upload_by__username=username).values("file_id")
                         file_ids =[id["file_id"] for id in file_ids]
                         not_found_movie=[]
                         found=[]
                         bulk_list = list()
                         for data in response["data"]["files"]:
                              if int(data["id"]) not in file_ids:
                                   name = data["filename"].split("(")[0]
                                   year = data["filename"].split("(")[1].split(")")[0]
                                   url = f"{settings.OMDB_API}?t={name}&y={year}&plot=full&apikey={settings.OMDB_API_KEY}"
                                   res = requests.request("GET", url).json()
                                   if "Error" in res:
                                        not_found_movie.append({"name":name,"year":year})
                                   else:
                                        found.append({"name":name,"year":year})
                                        size=str(round(int(data["fileSize"])/(1024*1024*1024),2))+" GB"
                                        date_object = datetime.strptime(res["Released"], "%d %b %Y")
                                        release_date = date_object.strftime("%Y-%m-%d")
                                        bulk_list.append(MovieInfo(name=res["Title"],release_date=release_date,slug="null",trailer_url="null",download_url="null",
                                                                 file_id=data["id"],thumbnail_url=res["Poster"],
                                                                 cast=res["Actors"],size=size,upload_source_code=data["shortUrl"],
                                                                 upload_by_id=cyber_user["id"],source_type_id=cyber_user["source_type_id"],
                                                                 duration=res["Runtime"],genres=res["Genre"],
                                                                 description=res["Plot"], imdb=res["imdbRating"]))
                         MovieInfo.objects.bulk_create(bulk_list)
                         return HttpResponse(json.dumps({"data":[{"not found":not_found_movie,"found":found}], "status": 1, "message": "Movie fetch successfully."}))
                    else:
                         return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Username not found or de-active or is not movie account"}))
               else:
                    return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Username not found."}))
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))


@csrf_exempt
def web_scheduler(request):
     try:
          with transaction.atomic():
               data = json.loads(request.body)
               username = data["username"]
               password = data["password"]
               if username and password:
                    cyber_user = CyberUser.objects.filter(username=username,is_active=True,is_web_account=True).values("id","source_type_id").first()
                    if cyber_user:
                         token_and_id = get_access_token(username, password)
                         token_and_id = json.loads(token_and_id)
                         if "msg" in token_and_id:
                              return HttpResponse(json.dumps({"data":[], "status": 1, "message": token_and_id["msg"]}))
                         access_token = token_and_id["access_token"]
                         account_id = token_and_id["account_id"]
                         url = f"{settings.CYBER_FILE}/folder/listing?access_token={access_token}&account_id={account_id}"
                         response = requests.request("GET", url).json()
                         file_ids = MovieInfo.objects.filter(upload_by__username=username).values("file_id")
                         file_ids =[id["file_id"] for id in file_ids]
                         not_found_movie=[]
                         found=[]
                         bulk_list = list()
                         web_data=[]
                         for data in response["data"]["files"]:
                              if int(data["id"]) not in file_ids:
                                   if '[' in data["filename"]:
                                        name = data["filename"].split("(")[0]
                                        year = data["filename"].split("(")[1].split(")")[0]
                                        season = data["filename"].split("[")[1].split("-")[0]
                                        episode =  data["filename"].split("-")[1].split("]")[0]
                                        upload_source_code = data["shortUrl"]
                                        if web_data:
                                             for web_data_ in web_data:
                                                  for key,value in web_data_.items():
                                                       if str(value) == str(web_data_[key]):
                                                            if key == "episode":
                                                                 web_data_["episode"].append(
                                                                      {
                                                                           "ep": episode,
                                                                           "code": upload_source_code
                                                                      }
                                                                 )
                                        else:
                                             web_data.append({"name":name,
                                                       "season":season,
                                                       "episode":[
                                                            {
                                                                 "ep": episode,
                                                                 "code": upload_source_code
                                                            },
                                                       ]})

                         for web in web_data:
                              is_exits  = MovieInfo.objects.filter(name=web["name"]).first()
                              if is_exits is None:
                                   bulk_list.append(MovieInfo(name=web["name"],slug="null",trailer_url="null",download_url="null",
                                                                           file_id=0,thumbnail_url="",
                                                                           cast="",size="",upload_source_code=0,
                                                                           upload_by_id=cyber_user["id"],source_type_id=cyber_user["source_type_id"],
                                                                           duration="",genres="",
                                                                           description="", imdb="",is_web=True,season=web["season"],episode=web["episode"]))
                                   found.append(web["name"])
                         MovieInfo.objects.bulk_create(bulk_list)

                         #                url = f"{settings.OMDB_API}?t={name}&y={year}&plot=full&apikey={settings.OMDB_API_KEY}"
                         #                res = requests.request("GET", url).json()
                         #                if "Error" in res:
                         #                     not_found_movie.append({"name":name,"year":year})
                         #                else:
                         #                     found.append({"name":name,"year":year})
                         #                     size=str(round(int(data["fileSize"])/(1024*1024*1024),2))+" GB"
                         #                     date_object = datetime.strptime(res["Released"], "%d %b %Y")
                         #                     release_date = date_object.strftime("%Y-%m-%d")
                         #                     bulk_list.append(MovieInfo(name=res["Title"],release_date=release_date,slug="null",trailer_url="null",download_url="null",
                         #                                              file_id=data["id"],thumbnail_url=res["Poster"],
                         #                                              cast=res["Actors"],size=size,upload_source_code=data["shortUrl"],
                         #                                              upload_by_id=cyber_user["id"],source_type_id=cyber_user["source_type_id"],
                         #                                              duration=res["Runtime"],genres=res["Genre"],
                         #                                              description=res["Plot"], imdb=res["imdbRating"]))
                         # MovieInfo.objects.bulk_create(bulk_list)
                         return HttpResponse(json.dumps({"data":[{"not found":not_found_movie,"found":found}], "status": 1, "message": "Movie fetch successfully."}))
                    else:
                         return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Username not found or de-active or is not web account"}))
               else:
                    return HttpResponse(json.dumps({"data":[], "status": 1, "message": "Username not found."}))
     except Exception as e:
          manager.create_from_exception(e)
          return HttpResponse(json.dumps({"data":[], "status": 0, "message": str(e)}))


def get_access_token(username,password):
     try:
          url = f"{settings.CYBER_FILE}/authorize?username={username}&password={password}"
          response = requests.request("GET", url).json()
          account_id = response["data"]["account_id"]
          access_token = response["data"]["access_token"]
          CyberUser.objects.filter(username=username).update(cyber_access_token=access_token)
          return json.dumps({"access_token":access_token,"account_id":account_id})
     except Exception as e:
          manager.create_from_exception(e)
          return json.dumps({"msg":"Something went wrong in get access token"})


@csrf_exempt
def data_transfer(request):
     try:
          fields_to_retrieve = [field.name for field in MovieInfo._meta.fields if field.name not in ['release_date','published'] ]
          movies = MovieInfo.objects.all().annotate(release_date_str=Cast('release_date', CharField()),published_str=Cast('published', CharField())).values(*fields_to_retrieve,"release_date_str","published_str")
          movies_info = {"data":list(movies)}
          url = f"{settings.LIVE_URL}/premiear/data_retrieve/"
          headers = {'Content-Type': 'application/json'}
          response = requests.post(url, data=json.dumps(movies_info), headers=headers).json()
          return JsonResponse(response)
     except Exception as e:
          print(e)
          manager.create_from_exception(e)
          return JsonResponse({"msg":"Something went wrong in data transfer"})


@csrf_exempt
def data_retrieve(request):
     try:
          data = json.loads(request.body)
          all_movie =[i["name"] for i in list(MovieInfo.objects.values("name"))]
          add_new_movie = []
          already_exits = []
          for i in data["data"]:
               if i.get("name") not in all_movie:
                    data_ = {
                         'name':i.get("name"),
                         'slug':i.get("slug"),
                         'trailer_url':i.get("trailer_url"),
                         'download_url':i.get("download_url"),
                         'thumbnail_url':i.get("thumbnail_url"),
                         'source_url':i.get("source_url"),
                         'screenshots':i.get("screenshots"),
                         'source_type_id':int(i.get("source_type")),
                         'duration':i.get("duration"),
                         'size':i.get("size"),
                         'description':i.get("description"),
                         'language':i.get("language"),
                         'genres':i.get("genres"),
                         'cast':i.get("cast"),
                         'upload_source_code':i.get("upload_source_code"),
                         'file_id':i.get("file_id"),
                         'username':i.get("username"),
                         'account_id':i.get("account_id"),
                         'upload_by_id':int(i.get("upload_by")),
                         'imdb':i.get("imdb"),
                         'is_web':i.get("is_web"),
                         'season':i.get("season"),
                         'episode':i.get("episode"),
                         'release_date':i.get("release_date_str"),
                         'published':i.get("published_str"),
                         }
                    new_instance = MovieInfo(**data_)
                    new_instance.save()
                    add_new_movie.append(i.get("name"))
                    all_movie.append(i.get("name"))
               else:
                    already_exits.append(i.get("name"))
          return JsonResponse({"msg":"Data Retrieve successfully","total_add_movie":len(add_new_movie),"already_exits":already_exits,"add_new_movie":add_new_movie})
     except Exception as e:
          manager.create_from_exception(e)
          return JsonResponse({"msg":"Something went wrong in data transfer"})
