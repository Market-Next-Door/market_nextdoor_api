from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ...serializers import CustomerSerializer
from ...models import Customer


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
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_details(request, customer_id):

  try:
    customer = Customer.objects.get(pk=customer_id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_one_customer(customer)
  
  elif request.method == 'PUT':
    return update_one_customer(customer, request)
  
  elif request.method == 'DELETE':
    return delete_customer(customer)
  
def get_one_customer(customer):
  serializer = CustomerSerializer(customer)
  return Response(serializer.data)

def update_one_customer(customer, request):
    customer_data = CustomerSerializer(customer, data=request.data, partial=True)
    if customer_data.is_valid():
      customer_data.save()
      return Response(customer_data.data)
    return Response(customer_data.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_customer(customer):
  customer.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)