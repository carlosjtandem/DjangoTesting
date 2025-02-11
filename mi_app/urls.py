# from django.urls import path
# from .views import hola_mundo

# urlpatterns = [
#     path('', hola_mundo),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
