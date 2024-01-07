from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import PreorderSerializer, CustomerSerializer, Preorder_testSerializer
from ..models import Preorder, Customer, Preorder_test, Preorder_testItem


@api_view(['GET', 'POST'])
def preorder_list(request, customer_id):
  try:
    check_customer = Customer.objects.get(pk=customer_id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    return get_preorder_list(request, check_customer)
  elif request.method == 'POST':
    return create_preorder(request)

def get_preorder_list(request, check_customer):
  preorders = Preorder.objects.filter(customer=check_customer)
  serializer = PreorderSerializer(preorders, many=True)
  return Response(serializer.data)

def create_preorder(request):
  serializer = PreorderSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def preorder_details(request, customer_id, preorder_id):
  try:
    customer = Customer.objects.get(pk=customer_id)
  except customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  try:
    preorder = Preorder.objects.get(pk=preorder_id, customer=customer)
  except Preorder.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_preorder_details(preorder)
  elif request.method == 'PUT':
    return update_preorder(preorder, request.data)
  elif request.method == 'DELETE':
    return delete_preorder(preorder)
  
def get_preorder_details(preorder):
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
  return Response(status=status.HTTP_204_NO_CONTENT)


#manytomany views testing
@api_view(['GET', 'POST'])
def preorder_test_list(request, customer_id):
  try:
    check_customer = Customer.objects.get(pk=customer_id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    return get_preorder_test_list(request, check_customer)
  elif request.method == 'POST':
    return create_preorder_test(request, check_customer)

def get_preorder_test_list(request, check_customer):
  preorder_tests = Preorder_test.objects.filter(customer=check_customer)
  serializer = Preorder_testSerializer(preorder_tests, many=True)
  return Response(serializer.data)

def create_preorder_test(request, check_customer):
  serializer = Preorder_testSerializer(data=request.data)
  if serializer.is_valid():
    preorder = serializer.save()

    items = request.data.get('items', [])
    for item in items:
      Preorder_testItem.objects.create(
        preorder=preorder,
        item_id=item['item'],
        quantity=item['quantity']
      )
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
