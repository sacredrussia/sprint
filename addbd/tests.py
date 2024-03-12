from rest_framework.test import APITestCase
from django.urls import reverse
from . import views
import json

from .models import Passes, Coordinates, Images, Users
class PassesTests(APITestCase):
    def get_status(self):
        response = self.client.get(reverse('passes_list'))
        print(response)
