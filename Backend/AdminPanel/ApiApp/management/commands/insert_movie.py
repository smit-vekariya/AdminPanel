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
import yt_dlp

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                MovieInfo.objects.all().delete()
                not_found_movie=[]
                found=[]
                request_data= requests.request("GET","https://hsdhsgg.pages.dev/test.json")
                movie_data = request_data.json()
                bulk_list=[]
                i=0
                for data in movie_data["AllMovieDataList"]:
                    name = data["movieName"].split("(")[0]
                    year = data["movieName"].split("(")[1].split(")")[0]
                    url = f"{settings.OMDB_API}?t={name}&y={year}&plot=full&apikey={settings.OMDB_API_KEY}"
                    res = requests.request("GET", url).json()
                    if "Error" in res:
                        not_found_movie.append({"name":name,"year":year})
                    else:
                        found.append({"name":name,"year":year})
                        if res["Released"] != 'N/A':
                            date_object = datetime.strptime(res["Released"], "%d %b %Y")
                            release_date = date_object.strftime("%Y-%m-%d")
                        else:
                            release_date=None
                        trailer_url = get_trailer_url(data["movieName"]) 
                        bulk_list.append(MovieInfo(name=data["movieName"],release_date=release_date,download_url=data["server3"],
                                                    thumbnail_url=data["ImageUrlVertical"],trailer_url=trailer_url,
                                                    cast=res["Actors"],
                                                    language=res["Language"],duration=res["Runtime"],genres=res["Genre"],
                                                    description=res["Plot"], imdb=res["imdbRating"]))
                    if i == 10:
                        break
                    i+=1
                MovieInfo.objects.bulk_create(bulk_list)
        except Exception as e:
            print(e)
        print(not_found_movie)
                

def get_trailer_url(name):
    url_data = name + " trailer"
    url_data = url_data.replace(" ","%20").replace("\"","%22")
    search_song_url = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={url_data}")
    video_ids = re.findall(r"watch\?v=(\S{11})", search_song_url.read().decode())
    url_data = str("https://www.youtube.com/watch?v=" + video_ids[0])
    return url_data
   


#   {
#     'id': '2573',
#     'ImageUrlHorizontal': 'https://api.ringzstudio.com/Poster/Movies/H1/8v8iol5w498nrv46g.jpg',
#     'ImageUrlVertical': 'https://api.ringzstudio.com/Poster/Movies/V1/8zx5jdhlziixlwv6g.jpg',
#     'movieName': 'Ghost In The Shell (2017)',
#     'htmlFile': 'https://www.5305',
#     'directOne': 'Dubbed',
#     'directSecond': 'G4VmJcZR0Yg',
#     'rating': 'Hindi',
#     'catergory': 'Adult',
#     'Industry': 'Hollywood',
#     'hub': 'FALSE',
#     'tape': 'https://streamtape.site/v/gao30428e8UgMb/Ghost_in_the_Shell_%282017%29_5305.mkv.mp4',
#     'server3': 'http://mvsold.aapkipooja.com/mvs/Ghost%20in%20the%20Shell%20(2017)%205305.mkv',
#     'server4': 'FALSE',
#     '480p': 'FALSE',
#     '480pS1': 'FALSE',
#     '480pS2': 'FALSE',
#     '480pS3': 'FALSE',
#     '480pS4': 'FALSE'
#   },