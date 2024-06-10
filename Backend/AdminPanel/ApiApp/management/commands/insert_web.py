from django.core.management.base import BaseCommand
import requests
from ApiApp.models import MovieInfo
from django.conf import settings
from datetime import datetime
from django.db import transaction
from rest_framework.views import APIView
from django.http import HttpResponse
import requests
import json
from Account import manager
from datetime import datetime
import urllib.request
import re

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            request_data= requests.request("GET","https://hsdhsgg.pages.dev/srs.json")
            movie_data = request_data.json()
            i=0
            for data in movie_data["webSeriesDataList"]:
                if not MovieInfo.objects.filter(static_id=data["id"]).exists() and data["Industry"] not in ["Bengali","Adult"]:

                    trailer_url = get_trailer_url(data["movieName"])
                    episode =[]
                    for key ,value in (data["episodeServer4"]).items():
                        episode.append({
                            "name":data["movieName"] + "(E"+key+")",
                            "file_id":data["id"] + key
                        })
                    MovieInfo.objects.create(name=data["movieName"],is_web=True,
                                                thumbnail_url=data["ImageUrlVertical"],trailer_url=trailer_url,static_id= data["id"],season=data["pathName"],
                                                language=data["rating"],genres=data["directOne"],industry=data["Industry"],imdb=data["imbd"],episode=episode,all_episode=data["episodeServer4"]
                                                )
                    i+=1
                    print(i, data["movieName"])
        except Exception as e:
            print(e)


def get_trailer_url(name):
    try:
        url_data = name + " trailer"
        url_data = url_data.replace(" ","%20").replace("\"","%22")
        search_song_url = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={url_data}")
        video_ids = re.findall(r"watch\?v=(\S{11})", search_song_url.read().decode())
        url_data = str("https://www.youtube.com/watch?v=" + video_ids[0])
        return url_data
    except Exception as e:
        print(e)
        return  None


