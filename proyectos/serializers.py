from rest_framework import serializers
from .models import Proyectos

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'fecha_creacion')
        read_only_fields = ('fecha_creacion', )

# Los serializers en Django REST Framework son clases que se encargan de convertir datos complejos (como modelos de Django) en formatos simples como JSON, y viceversa.