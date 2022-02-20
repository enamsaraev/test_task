from rest_framework import serializers
from . import models


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()


# class CleanDataSerializer(serializers.Serializer):

