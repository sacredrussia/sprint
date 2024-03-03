from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Passes, Coordinates, Users, Images
from rest_framework import generics
from .serializers import PassesSerializer


class PassesAPIView(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            inst = Passes.objects.get(pk=pk)
        except:
            return Response({0: 'Object does not exists'})
        user_list = Users.objects.get(pk=inst.user_id)
        coord_list = Coordinates.objects.get(pk=inst.coordinates_id)
        image_list = Images.objects.all()
        image_list_filter = image_list.filter(passes_id=inst.pk).order_by('pk')
        return Response({'passes': model_to_dict(inst),
                         'users': model_to_dict(user_list),
                         'coordinates': model_to_dict(coord_list),
                         'image1': model_to_dict(image_list_filter[0]),
                         'image2': model_to_dict(image_list_filter[1])})

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
            return Response({'error': 'Method GET not allowed'})
        try:
            inst = Passes.objects.get(pk=pk)
            if inst.status != stat:
                return Response({0: 'Incorrect moderation status'})
        except:
            return Response({0: 'Object does not exists'})

        set_coords = request.data['coords']
        set_level = request.data['level']
        set_user = request.data['user']
        list_image = request.data['images']

        coords = Coordinates.objects.get(pk=inst.coordinates_id)
        coords.latitude = set_coords['latitude']
        coords.longitude = set_coords['longitude']
        coords.height = set_coords['height']
        coords.save()

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
        b = 0
        for set_image in list_image:
            one_mod = set_mod_images[b]
            get_mod = Images.objects.get(pk=one_mod.pk)
            get_mod.name = set_image['title']
            get_mod.save()
            b = b + 1
        return Response(1)


class EmailAPIView(APIView):
    def get(self, request, **kwargs):
        email = kwargs.get('email', None)
        if not email:
            return Response({'error': 'Method PUT not allowed'})
        try:
            inst = Users.objects.get(email=email)
        except:
            return Response({0: 'Object does not exists'})
        user_list = inst
        passes = Passes.objects.all()
        passes_list = passes.filter(user_id=inst.pk)
        set_passes = []
        set_images = []
        set_coords = []
        for j in passes_list:
            e = model_to_dict(j)
            print(e)
            set_passes.append(e)
            print(set_passes)
            coords = Coordinates.objects.all()
            coord_list = coords.filter(pk=j.coordinates_id).order_by('pk')
            for f in coord_list:
                h = model_to_dict(f)
                set_coords.append(h)
            image_list = Images.objects.all()
            image_list_filter = image_list.filter(passes_id=j.pk)
            for i in image_list_filter:
                c = model_to_dict(i)
                set_images.append(c)

        return Response({'passes': set_passes,
                         'users': model_to_dict(user_list),
                         'coordinates': set_coords,
                         'images': set_images})

    def post(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if not email:
            return Response({'error': 'Method POST not allowed'})
        try:
            inst = Users.objects.get(email=email)
        except:
            return Response({0: 'Object does not exists'})

        set_coords = request.data['coords']
        set_level = request.data['level']
        list_image = request.data['images']

        coords_new = Coordinates.objects.create(
            latitude=set_coords['latitude'],
            longitude=set_coords['longitude'],
            height=set_coords['height']
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
            user_id=inst.pk
        )
        for set_image in list_image:
            image_new = Images.objects.create(
                name=set_image['title'],
                passes_id=passes_new.pk
            )

        return Response({'posts': 200})


