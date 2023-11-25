from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import TaskSerializer

from .models import Tasks

class CarListAPIview(ListCreateAPIView):
    serializer_class = TaskSerializer
    model = Tasks
    queryset = Tasks.objects.all()

# Create your views here.
