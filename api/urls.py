from django.urls import path
from .views import analizar_imagen

urlpatterns = [
    path('analizar-imagen', analizar_imagen),
]