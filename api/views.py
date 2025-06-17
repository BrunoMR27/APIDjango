from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
import os
import random

@api_view(['POST'])
def analizar_imagen(request):
    if 'imagen' not in request.FILES:
        return Response({'error': 'No se recibió ninguna imagen'}, status=400)

    imagen = request.FILES['imagen']
    path = default_storage.save('tmp/' + imagen.name, imagen)
    ruta_completa = os.path.join(default_storage.location, path)

    # 🔽 Simulación de análisis de IMC
    imc = round(random.uniform(16.0, 35.0), 1)

    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif 18.5 <= imc < 25:
        clasificacion = "Peso normal"
    elif 25 <= imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    resultado = f"IMC: {imc} - {clasificacion}"

    return Response({'resultado': resultado})

