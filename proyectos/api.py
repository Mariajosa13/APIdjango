from .serializers import ProyectoSerializer
from .models import Proyectos
from rest_framework import viewsets, permissions

class ProyectoViewSet(viewsets.ModelViewSet): # vista basada en clases, que maneja automáticamente: GET, POST, DELETE, PUT/PATCH
    queryset = Proyectos.objects.all() # se indica a la vista que trabaje con todos los proyectos de la base de datos.
    permission_classes = [permissions.AllowAny] # Esto indica que cualquier persona puede acceder a esta API (no necesita estar autenticada).
    serializer_class = ProyectoSerializer # Indicas qué serializer se usará para convertir los objetos del modelo a JSON y viceversa.

# La clase `ProyectoViewSet` hereda de `ModelViewSet`, que es una vista genérica de Django REST Framework que proporciona la implementación básica para las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo.