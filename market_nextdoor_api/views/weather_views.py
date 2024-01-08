from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import os


# OpenWeather API
@api_view(['GET'])
def weather(request):
    if request.method == 'GET':
        zipcode = request.GET.get('zipcode', '80020')
        return get_weather(request, zipcode)

def get_weather(request, zipcode):
    appid = '8fe63c807f5a5c8cce5e070949033a96'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': zipcode, 'appid': appid}

    r = requests.get(url=URL, params=PARAMS)
    
    if r.status_code == 200:
        res = r.json()
        description = res['weather'][0]['description']
        temp = round(res['main']['temp'] - 255.37)

        return JsonResponse({'description': description, 'temp': temp})
    else:
        error_message = f"Error: {r.status_code}"
        return JsonResponse({'error': error_message}, status=500)
  