import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ApiApp.models import MovieInfo
from Account import manager
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
          movies = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published").order_by('-release_date')[:3]
          source_data = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published")
          movies_info = {"data": [{
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
               }],"status": 1, "message":"success"}
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
                    "source_type":data["source_type__name"],
                    "duration":data["duration"],
                    "description":data["description"],
                    "language":str(data["language"]),
                    "genres":data["genres"],
                    "cast":data["cast"],
               })

          for data in source_data:
               if data["source_type__name"]=="NetFlix":
                    index = 1
               elif data["source_type__name"]=="Amazon":
                    index = 2
               elif data["source_type__name"]=="Disney":
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
               movies = MovieInfo.objects.values("id","name","slug","release_date","trailer_url","download_url","thumbnail_url","source_url","source_url","screenshots","source_type__name","duration","description","language","genres","cast","published").order_by('-release_date')[:10]
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


# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup

# import codecs

# import re

# from webdriver_manager.chrome import ChromeDriverManager


# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# val = "https://cyberfile.me/b7ip"

# wait = WebDriverWait(driver, 10)

# driver.get(val)


# get_url = driver.current_url
# # wait.until(EC.url_to_be(val))
# wait.until_not(EC.url_to_be(val))

# print(get_url)
# print(val)
# if get_url == val:
#     print("-----------")


# page_source = driver.page_source
# # print(page_source)
# soup = BeautifulSoup(page_source,features="html.parser")
# pp =soup.find('div', class_='responsiveMobileMargin')
# ps= str(pp)
# ps2 = ps.split("openUrl('")[1]
# ps3 = ps2.split("');")[0]
# print(ps3)

# # with open("data/cyberfile_____1__.html", "w") as f:
# #     f.write(page_source)

