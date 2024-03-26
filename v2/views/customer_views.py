from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import CustomerSerializer, PreorderSerializer
from ..models import Customer, Market, Preorder, PreorderItem, Item
import pdb


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


# Customer Preorders
@api_view(['GET', 'POST'])
def preorder_by_customer_list(request, market_id, customer_id):
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
  except customer.DoesNotExist:
    return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    return get_preorder_list(request, customer)
  elif request.method == 'POST':
    return create_preorder(request, customer)

def get_preorder_list(request, customer):
  preorders = Preorder.objects.filter(customer=customer)
  serializer = PreorderSerializer(preorders, many=True)
  return Response(serializer.data)

def create_preorder(request, customer):
  serializer = PreorderSerializer(data=request.data)
  if serializer.is_valid():
    preorder = serializer.save(customer=customer)
    response = preorder_item_helper(request, preorder, serializer)
    return response
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
def preorder_item_helper(request, preorder, serializer):
  items = request.data.get('items', [])
  for item_data in items:
    try:
      item = Item.objects.get(pk=item_data["item"])
    except Item.DoesNotExist:
      return Response({"error":f'Item {item_data["item"]} does not exist'}, status=status.HTTP_404_NOT_FOUND)
      
    PreorderItem.objects.create(
      preorder=preorder,
      item_id=item.id,
      quantity_requested=item_data['quantity']
      )
  return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def preorder_by_customer_details(request, market_id, customer_id, preorder_id):
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
  except customer.DoesNotExist:
    return Response({"error": "customer not found."}, status=status.HTTP_404_NOT_FOUND)
  try:
    preorder = Preorder.objects.get(pk=preorder_id, customer=customer)
  except Preorder.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_preorder_customer_list_details(preorder)
  elif request.method == 'PUT':
    return update_preorder(preorder, request.data)
  elif request.method == 'DELETE':
    return delete_preorder(preorder)

def get_preorder_customer_list_details(preorder):
  serializer = PreorderSerializer(preorder)
  return Response(serializer.data)

def update_preorder(preorder, data):
  preorder_data = PreorderSerializer(preorder, data=data, partial=True)
  if preorder_data.is_valid():
    preorder_data.save()
    return Response(preorder_data.data)
  return Response(status=status.HTTP_400_BAD_REQUEST) 

def delete_preorder(preorder): 
  preorder.delete()
  return Response({'message': "deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
