from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Passes, Coordinates, Users, Images
from .serializer import PassesSerializer


# class PassesAPIView(generics.ListAPIView):
# queryset = Passes.objects.all()
# serializer_class = PassesSerializer


class PassesAPIView(APIView):
    def post(self, request):
        set_coords = request.data['coords']
        set_level = request.data['level']
        set_user = request.data['user']
        list_image = request.data['images']

        coords_new = Coordinates.objects.create(
            latitude=set_coords['latitude'],
            longitude=set_coords['longitude'],
            height=set_coords['height']
        )

        user_new = Users.objects.create(
            email=set_user['email'],
            fam=set_user['fam'],
            name=set_user['name'],
            otc=set_user['otc'],
            phone=set_user['phone'],
        )

        passes_new = Passes.objects.create(
            beautyTitle=request.data['beauty_title'],
            title=request.data['title'],
            other_titles=request.data['other_titles'],
            connect=request.data['connect'],
            add_time=request.data['add_time'],
            level_winter=set_level['winter'],
            level_summer=set_level['summer'],
            level_autumn=set_level['autumn'],
            level_spring=set_level['spring'],
            status='new',
            coordinates_id=coords_new.pk,
            user_id=user_new.pk
        )

        for set_image in list_image:
            image_new = Images.objects.create(
                name=set_image['title'],
                passes_id=passes_new.pk
            )

        return Response(200)
