from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Passes, Coordinates
from .serializer import PassesSerializer


#class PassesAPIView(generics.ListAPIView):
    #queryset = Passes.objects.all()
    #serializer_class = PassesSerializer


class PassesAPIView(APIView):
    def get(self, request):
        lst = Passes.objects.all().values
        return Response({'posts': list(lst)})

    def post(self, request):
        set1 = request.data['coords']
        coords_new = Coordinates.objects.create(
            latitude=set1['latitude'],
            longitude=set1['longitude'],
            height=set1['height']
        )
        passes_new = Passes.objects.create(
            beautyTitle=request.data['beautyTitle'],
            add_time=request.data['add_time'],



        )


        return Response({'post': model_to_dict(coords_new)})

