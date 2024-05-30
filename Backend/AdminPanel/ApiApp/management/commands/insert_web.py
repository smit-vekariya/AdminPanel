from django.core.management.base import BaseCommand
import requests
from ApiApp.models import MovieInfo
from django.conf import settings
from datetime import datetime 
from django.db import transaction

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                # MovieInfo.objects.all().delete()
                not_found_movie=[]
                found=[]
                request_data= requests.request("GET","https://hsdhsgg.pages.dev/srs.json")
                movie_data = request_data.json()
                print(str(movie_data)[0:10000])
                # bulk_list=[]
                # for data in movie_data["AllMovieDataList"]:
                #     name = data["movieName"].split("(")[0]
                #     year = data["movieName"].split("(")[1].split(")")[0]
                #     url = f"{settings.OMDB_API}?t={name}&y={year}&plot=full&apikey={settings.OMDB_API_KEY}"
                #     res = requests.request("GET", url).json()
                #     if "Error" in res:
                #         not_found_movie.append({"name":name,"year":year})
                #     else:
                #         found.append({"name":name,"year":year})
                #         if res["Released"] != 'N/A':
                #             date_object = datetime.strptime(res["Released"], "%d %b %Y")
                #             release_date = date_object.strftime("%Y-%m-%d")
                #         else:
                #             release_date=None
                #         bulk_list.append(MovieInfo(name=data["movieName"],release_date=release_date,download_url=data["server3"],
                #                                     thumbnail_url=data["ImageUrlVertical"],
                #                                     cast=res["Actors"],
                #                                     language=res["Language"],duration=res["Runtime"],genres=res["Genre"],
                #                                     description=res["Plot"], imdb=res["imdbRating"]))
                # MovieInfo.objects.bulk_create(bulk_list)
        except Exception as e:
            print(e)
        print(not_found_movie)
        print(found)
                


# {
#   'webSeriesDataList': [
#     {
#       'id': '2',
#       'ImageUrlHorizontal': 'https://api.aapkipooja.com/Poster/Series/H1/movgtfxupezukgb6g.jpg',
#       'ImageUrlVertical': 'https://api.aapkipooja.com/Poster/Series/V1/xbooywdfhb8w0lr6g.jpg',
#       'movieName': '13 Reasons Why Season 1',
#       'htmlFile': 'https://www.5310',
#       'directOne': 'Popular,Drama',
#       'directSecond': 'HC765gMqmew',
#       'imbd': '7.7',
#       'rating': 'Dual',
#       'catergory': 'webSeries',
#       'Industry': 'webSeries',
#       'keyName': '13 Reasons Why',
#       'pathName': 'S1',
#       'EpisodeTape': {
#         '1': 'https://streamtape.site/v/kqVBoQ0Y4OCOkMM/13.Reasons.Why.S01E01_6617.mkv.mp4',
#         '2': 'https://streamtape.site/v/Bbd96ozVrXT29z/13.Reasons.Why.S01E02_6618.mkv.mp4',
#         '3': 'https://streamtape.site/v/vgAJLzx6wbU4exW/13.Reasons.Why.S01E03_6619.mkv.mp4',
#         '4': 'https://streamtape.site/v/BAAr1majRdfygpP/13.Reasons.Why.S01E04_6620.mkv.mp4',
#         '5': 'https://streamtape.site/v/OJLB0Pb4XJfZr0M/13.Reasons.Why.S01E05_6621.mkv.mp4',
#         '6': 'https://streamtape.site/v/6RvgaBARYkceAp/13.Reasons.Why.S01E06_6622.mkv.mp4',
#         '7': 'https://streamtape.site/v/mwxD2dKVGKIVxW/13.Reasons.Why.S01E07_6623.mkv.mp4',
#         '8': 'https://streamtape.site/v/ereKYPm9vXf2Y9/13.Reasons.Why.S01E08_6624.mkv.mp4',
#         '9': 'https://streamtape.site/v/ab6V63Qm7gIxDG7/13.Reasons.Why.S01E09_6625.mkv.mp4',
#         '10': 'https://streamtape.site/v/6b4aMgZvjaf9JkR/13.Reasons.Why.S01E10_6626.mkv.mp4',
#         '11': 'https://streamtape.site/v/wY1OpkQ49GiJydM/13.Reasons.Why.S01E11_6627.mkv.mp4',
#         '12': 'https://streamtape.site/v/e2aVqKy0Z9cYG06/13.Reasons.Why.S01E12_6628.mkv.mp4',
#         '13': 'https://streamtape.site/v/qOZ6YDAxmrtz3Qo/13.Reasons.Why.S01E13_6629.mkv.mp4'
#       },
#       'EpisodeHub': {
        
#       },
#       'episodeServer3': {
        
#       },
#       'episodeServer4': {
#         '1': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E01%206617.mkv',
#         '2': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E02%206618.mkv',
#         '3': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E03%206619.mkv',
#         '4': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E04%206620.mkv',
#         '5': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E05%206621.mkv',
#         '6': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E06%206622.mkv',
#         '7': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E07%206623.mkv',
#         '8': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E08%206624.mkv',
#         '9': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E09%206625.mkv',
#         '10': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E10%206626.mkv',
#         '11': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E11%206627.mkv',
#         '12': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E12%206628.mkv',
#         '13': 'http://srsold.aapkipooja.com/srs1/13.Reasons.Why.S01E13%206629.mkv'
#       }
#     },
    
#   ]
# }