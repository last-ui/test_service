from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from picture.models import Picture


class PictureSerializer(ModelSerializer):

    description = serializers.CharField()
    image = Base64ImageField()

    class Meta:
        model = Picture
        fields = (
            "id",
            "description",
            "image",
        )
        read_only_fields = ("id",)
