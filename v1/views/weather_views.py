from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import os
from django.core.cache import cache


# OpenWeather API
@api_view(['GET'])
def weather(request):
    if request.method == 'GET':
        zipcode = request.GET.get('zipcode', '80020')
        
        cached_data = cache.get(zipcode + '_weather_data')

        if cached_data is not None:
            return JsonResponse(cached_data, safe=False)
        else:
            weather_data = get_weather(request, zipcode)

            cache.set(zipcode + '_weather_data', weather_data, 60 * 15)

            return JsonResponse(weather_data, safe=False)

def get_weather(request, zipcode):
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': zipcode, 'appid': WEATHER_API_KEY}

    r = requests.get(url=URL, params=PARAMS)
    
    if r.status_code == 200:
        res = r.json()
        description = res['weather'][0]['description']
        temp = round(res['main']['temp'] - 255.37)
        icon = res['weather'][0]['icon']

        weather_data = {'description': description, 'temp': temp, 'icon': icon}

        return weather_data
    else:
        error_message = f"Error: {r.status_code}"
        return {'error': error_message}
  