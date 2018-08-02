from django.contrib.auth.models import User, Group
from rest_framework import serializers
from stashology.stashology_app.models import (
    Brand,
    Color,
    Finish,
    Photo,
    Polish,
    Tag
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('url', 'name')


class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('url', 'name')


class FinishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finish
        fields = ('url', 'name')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'url', 'caption', 'lighting_type')


class PolishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Polish
        fields = ('id', 'url', 'name', 'brand', 'finish', 'colors', 'tags')
