from rest_framework import serializers
from .models import Proyectos

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'fecha_creacion')
        read_only_fields = ('fecha_creacion', )