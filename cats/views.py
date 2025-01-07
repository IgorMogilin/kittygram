from rest_framework import viewsets

from cats.models import Cat, Owner
from cats.serializers import CatSerializer, OwnerSerializer


class CatViewset(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewset(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
