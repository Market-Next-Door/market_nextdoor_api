from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import CustomerSerializer
from ..models import Customer, Market


@api_view(['GET', 'POST']) 
def customer_list(request):
  if request.method == 'GET':
    return get_customer_list(request)
  elif request.method == 'POST':
    return create_customer(request)
  
def get_customer_list(request):
  customers = Customer.objects.all()
  serializer = CustomerSerializer(customers, many=True)
  return Response(serializer.data)

def create_customer(request):
  serializer = CustomerSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_details(request, customer_id):
  customer = get_customer_object(customer_id)

  if request.method == 'GET':
    return get_customer_details(customer)
  elif request.method == 'PUT':
    return update_customer(customer, request)
  elif request.method == 'DELETE':
    return delete_customer(customer)
  
def get_customer_object(customer_id):
  try:
    return Customer.objects.get(pk=customer_id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

def get_customer_details(customer):
  serializer = CustomerSerializer(customer)
  return Response(serializer.data)

def update_customer(customer, request):
  customer_data = CustomerSerializer(customer, data=request.data, partial=True)
  if customer_data.is_valid():
    customer_data.save()
    return Response(customer_data.data)
  return Response(customer_data.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_customer(customer):
  customer.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

# Customer by Market
@api_view(['GET'])
def customers_by_market_list(request, market_id):
  # Input validation
  if not (isinstance(market_id, int) and market_id > 0):
    return Response({"error": "Invalid market id."}, status=status.HTTP_400_BAD_REQUEST)

  try:
    market = Market.objects.get(pk=market_id)
  except Market.DoesNotExist:
    return Response(stats=status.HTTP_404_NOT_FOUND)
  
  customers = market.customers.all()
  serializer = CustomerSerializer(customers, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def customer_by_market_details(request, customer_id, market_id):
  # Input validation
  if not (isinstance(market_id, int) and market_id > 0):
    return Response({"error": "Invalid market id."}, status=status.HTTP_400_BAD_REQUEST)
  if not (isinstance(customer_id, int) and customer_id > 0):
    return Response({"error": "Invalid customer id."}, status=status.HTTP_400_BAD_REQUEST)

  try:
    market = Market.objects.get(pk=market_id)
  except Market.DoesNotExist:
    return Response({"error": "Market not found."}, status=status.HTTP_404_NOT_FOUND)
  
  try:
    customer = market.customers.get(pk=customer_id)
  except Customer.DoesNotExist:
    return Response({"error": "customer not found."}, status=status.HTTP_404_NOT_FOUND)

  serializer = CustomerSerializer(customer)
  return Response(serializer.data)
