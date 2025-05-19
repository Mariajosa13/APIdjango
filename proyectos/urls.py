from rest_framework import routers # Importa el módulo de enrutamiento de Django REST Framework
from .api import ProyectoViewSet # Importa la vista del conjunto de proyectos
# El enrutador se encarga de crear automáticamente las URL para las vistas basadas en clases.

router = routers.DefaultRouter()

router.register('api/proyectos', ProyectoViewSet, 'proyectos') # Registra la vista del conjunto de proyectos en el enrutador, lo que significa que se crearán automáticamente las URL para las operaciones CRUD.
# 'api/proyectos' es la URL base para acceder a los proyectos a través de la API.
urlpatterns = router.urls