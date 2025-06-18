from rest_framework.decorators import api_view
from rest_framework.response import Response
import os, tempfile, random

@api_view(['POST'])
def analizar_imagen(request):
    try:
        if 'imagen' not in request.FILES:
            return Response({'error': 'No se recibió ninguna imagen'}, status=400)

        imagen = request.FILES['imagen']

        # Guardar temporalmente la imagen (funciona en Render)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
            for chunk in imagen.chunks():
                tmp.write(chunk)
            ruta_completa = tmp.name

        # Simulación del análisis de IMC
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
    
    except Exception as e:
        return Response({'error': f'Error interno: {str(e)}'}, status=500)
