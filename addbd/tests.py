from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from . import views
import json

from addbd.models import Passes, Coordinates, Images, Users


class PassesTest(APITestCase):
    def setUp(self):
        self.users = Users.objects.create(
            email='email_test',
            fam='fam_test',
            name='name_test',
            otc='otc_test',
            phone='+78888888888',
        )
        self.coords = Coordinates.objects.create(
            latitude=45.3842,
            longitude=7.1525,
            height=1200
        )
        self.one_passes = Passes.objects.create(
            beauty_title='beauty_title',
            title='title',
            other_titles='other_titles',
            connect='test_conn',
            add_time='2021-09-22T10:18:13',
            level_winter='test_winter',
            level_summer='test_summ',
            level_autumn='test_a',
            level_spring='test_s',
            status='new',
            coordinates_id=self.coords.pk,
            user_id=self.users.pk
        )
        self.image_new = Images.objects.create(
            name='title',
            passes_id=self.one_passes.pk
        )
        self.data = {
            "beauty_title": "пер. ",
            "title": "Пхияtest",
            "other_titles": "Триев1122",
            "connect": "",

            "add_time": "2021-09-22 13:18:13",
            "user": {"email": "email_test",
                     "fam": "Пупкин",
                     "name": "Василий",
                     "otc": "Иванович",
                     "phone": "+7 555 55 55"},

            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"},

            "level": {"winter": "",
                      "summer": "1А",
                      "autumn": "1А",
                      "spring": ""},

            "images": [{"data": "<картинка1>", "title": "Седловина3"}, {"data": "<картинка>", "title": "Подъём4"}]
        }
        self.data2 = {
            "beauty_title": "пер. ",
            "title": "Пхияtest",
            "other_titles": "Триев1test",
            "connect": "",

            "add_time": "2021-09-22 13:18:13",
            "user": {"email": "email_test12",
                     "fam": "Пупкин",
                     "name": "Василий",
                     "otc": "Иванович",
                     "phone": "+7 555 55 55"},

            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"},

            "level": {"winter": "",
                      "summer": "1А",
                      "autumn": "1А",
                      "spring": ""},

            "images": [{"data": "<картинка1>", "title": "Седловина3"}, {"data": "<картинка>", "title": "Подъём4"}]
        }
        print(f'passes set pk =', self.one_passes.pk)

    def test_get_status(self):
        response = self.client.get(reverse('get_passes_pk', kwargs={'pk': 1}))
        print(f'test1', response)

    def test_get_email(self):
        response = self.client.get(reverse('get_passes_email', kwargs={'email': self.users.email}))
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.json().get('email'), 'email_test')
        print(f'test2', response)

    def test_patch_id(self):
        response = self.client.patch(reverse('path_passes_pk', kwargs={'pk': 1}), self.data, format='json')
        print(f'test3', response)


class Passes2Test(APITestCase):
    def setUp(self):
        self.data2 = {
            "beauty_title": "пер. ",
            "title": "Пхияtest",
            "other_titles": "Триев1test",
            "connect": "",

            "add_time": "2021-09-22 13:18:13",
            "user": {"email": "email_test12",
                     "fam": "Пупкин",
                     "name": "Василий",
                     "otc": "Иванович",
                     "phone": "+7 555 55 55"},

            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"},

            "level": {"winter": "",
                      "summer": "1А",
                      "autumn": "1А",
                      "spring": ""},

            "images": [{"data": "<картинка1>", "title": "Седловина3"}, {"data": "<картинка>", "title": "Подъём4"}]
        }
    def test_post_passes(self):
        response = self.client.post(reverse('post_passes'), self.data2, format='json')
        print(f'test4', response)
