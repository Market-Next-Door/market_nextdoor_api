from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import MarketSerializer
from ..models import Market
import requests
import os


# Market CRUD functions (SRP)
@api_view(['GET', 'POST'])
def market_list(request):
  if request.method == 'GET':
    return get_market_list(request)
  elif request.method == 'POST':
    return create_market(request)

def get_market_list(request):
  markets = Market.objects.all()
  serializer = MarketSerializer(markets, many=True)
  return Response(serializer.data)

def create_market(request):
  serializer = MarketSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def market_details(request, market_id):
  market = get_market_object(market_id)

  if request.method == 'GET':
    return get_market_details(market)
  elif request.method == 'PUT':
    return update_market(market, request.data)
  elif request.method == 'DELETE':
    return delete_market(market)

def get_market_object(market_id):
  try:
    return Market.objects.get(pk=market_id)
  except Market.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

def get_market_details(market):
  serializer = MarketSerializer(market)
  return Response(serializer.data)

def update_market(market, data):
  market_data = MarketSerializer(market, data=data, partial=True)
  if market_data.is_valid():
    market_data.save()
    return Response(market_data.data)
  return Response(market_data.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_market(market):
  market.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)




#USDA Market locations 
def get_market_locations(request, zipcode, radius):
  USDA_API_KEY = os.environ.get('USDA_API_KEY')
  BASE_URL = "https://www.usdalocalfoodportal.com/api/farmersmarket/"
  request_url = f'{BASE_URL}?apikey={USDA_API_KEY}&zip={zipcode}&radius={radius}'
  head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
  try:
    response = requests.get(request_url, headers=head)
    response.raise_for_status()
    data = response.json()
    #Neat list comprehension - this parses the data coming in from the API, the syntax is a bit
    #different in that the iteration is after declaring the instance of a library on line 374
    refined_data = [
            {
                'market_name': item.get('listing_name', ''),
                'address': item.get('location_address', ''),
                'lat': item.get('location_x', ''),
                'lon': item.get('location_y', ''),
                'website': item.get('media_website', ''),
                'zipcode': item.get('location_zipcode', ''),
                'phone': item.get('contact_phone', '')
            }
            for item in data.get('data', [])
        ]

    return JsonResponse(refined_data, safe=False)
  except requests.RequestException:
    return JsonResponse({'error': str('There are no markets near you')}, status=404)
  