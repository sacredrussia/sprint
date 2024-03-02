from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Passes, Coordinates, Users, Images
from rest_framework import generics
from .serializers import PassesSerializer


class PassesAPIView(APIView):
    def get(self, request):
        p = Passes.objects.all()
        return Response({'posts': PassesSerializer(p, many=True).data})

    def post(self, request):
        serializer = PassesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

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
            beauty_title=request.data['beauty_title'],
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

        return Response({'posts': 200})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        stat = 'new'
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            inst = Passes.objects.get(pk=pk)
            if inst.status != stat:
                return Response({0: 'Incorrect moderation status'})
        except:
            return Response({0: 'Object does not exists'})
        print(inst)

        set_coords = request.data['coords']
        set_level = request.data['level']
        set_user = request.data['user']
        list_image = request.data['images']

        coords = Coordinates.objects.get(pk=inst.coordinates_id)
        coords.latitude = set_coords['latitude']
        coords.longitude = set_coords['longitude']
        coords.height = set_coords['height']
        coords.save()


        # user = Users.objects.get(pk=inst.user_id)
        # user_update = user.objects.update(
        #     email=set_user['email'],
        #     fam=set_user['fam'],
        #     name=set_user['name'],
        #     otc=set_user['otc'],
        #     phone=set_user['phone'],
        # )

        inst.beauty_title = request.data['beauty_title']
        inst.title = request.data['title']
        inst.other_titles = request.data['other_titles']
        inst.connect = request.data['connect']
        inst.add_time = request.data['add_time']
        inst.level_winter = set_level['winter']
        inst.level_summer = set_level['summer']
        inst.level_autumn = set_level['autumn']
        inst.level_spring = set_level['spring']
        inst.save()

        image = Images.objects.all()
        set_mod_images = image.filter(passes_id=inst.pk).order_by('pk')
        print(set_mod_images)
        b = 0
        for set_image in list_image:
            print(set_image)
            one_mod = set_mod_images[b]
            print(one_mod)
            get_mod = Images.objects.get(pk=one_mod.pk)
            print(one_mod)
            get_mod.name = set_image['title']
            get_mod.save()
            b = b + 1
        return Response(1)
