from rest framework import serializer
from .models import Project

class ProjectSerializer(serializer.ModelSerializer):

    class Meta:
        model = Project
        fields =('title','horario','clasificacion')

       