from rest_framework.serializers import ModelSerializer
from ApiApp.models import MovieInfo, AppInfo


class MovieInfoSerializer(ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = "__all__"

    def create(self, validated_data):
        # if not MovieInfo.objects.filter(name=validated_data["name"]).exists():
        #     return super().create(validated_data)
        return super().create(validated_data)


class AppInfoSerializer(ModelSerializer):
    class Meta:
        model = AppInfo
        fields = "__all__"