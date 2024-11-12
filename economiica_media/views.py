# from django.shortcuts import render
from rest_framework import generics
from .models import EconomiicaMedia
from .serializers import EconomiicaMediaSerializers


class EconomiicaMediaListCreateView(generics.ListCreateAPIView):
    queryset = EconomiicaMedia.objects.all()
    serializer_class = EconomiicaMediaSerializers


class EconomiicaMediaDeleteView(generics.DestroyAPIView):
    queryset = EconomiicaMedia.objects.all()
    serializer_class = EconomiicaMediaSerializers


# Add a class for the -timestamp
