from rest_framework.test import APITestCase
from django.urls import reverse
from addbd import views
import json

from addbd.models import Passes, Coordinates, Images, Users
class PassesTests(APITestCase):
    def get_status(self):
        response = self.client.get(reverse('passes_list'))
