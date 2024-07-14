from django.shortcuts import render
from rest_framework import generics

from main.models import Project
from main.serializers import ProjectSerializer


# Create your views here.
class ProjectListApi(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.filter()
        return queryset
