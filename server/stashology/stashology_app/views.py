from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from stashology.stashology_app.serializers import (
    BrandSerializer,
    ColorSerializer,
    FinishSerializer,
    GroupSerializer,
    PhotoSerializer,
    PolishSerializer,
    TagSerializer,
    UserSerializer,
)
from stashology.stashology_app.models import (
    Brand,
    Color,
    Finish,
    Photo,
    Polish,
    Tag
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class FinishViewSet(viewsets.ModelViewSet):
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PolishViewSet(viewsets.ModelViewSet):
    queryset = Polish.objects.all()
    serializer_class = PolishSerializer
