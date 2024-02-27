from django.shortcuts import render
from rest_framework import generics
from .models import Passes
from .serializer import PassesSerializer


class PassesAPIView(generics.ListAPIView):
    queryset = Passes.objects.all()
    serializer_class = PassesSerializer
