from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import PreorderSerializer, CustomerSerializer, Preorder2Serializer
from ..models import Preorder, Customer, Preorder2, Preorder2Item, Item
import pdb

#manytomany views testing
@api_view(['GET', 'POST'])
def preorder_customer_list(request, customer_id):
  try:
    check_customer = Customer.objects.get(pk=customer_id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    return get_preorder_list(request, check_customer)
  elif request.method == 'POST':
    return create_preorder(request, check_customer)

def get_preorder_list(request, check_customer):
  preorder_tests = Preorder2.objects.filter(customer=check_customer)
  serializer = Preorder2Serializer(preorder_tests, many=True)
  return Response(serializer.data)

def create_preorder(request, check_customer):
  serializer = Preorder2Serializer(data=request.data)
  if serializer.is_valid():
    preorder = serializer.save()
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
      return Response({"error":f'Item {item_data["item"]} does not exist'},
                      status=status.HTTP_404_NOT_FOUND)
      
    Preorder2Item.objects.create(
      preorder=preorder,
      item_id=item.id,
      quantity_requested=item_data['quantity']
      )
  return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def preorder_customer_details(request, customer_id, preorder_id):
  try:
    customer = Customer.objects.get(pk=customer_id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  try:
    preorder = Preorder2.objects.get(pk=preorder_id, customer=customer)
  except Preorder2.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_preorder_details(preorder)
  # elif request.method == 'PUT': #Do we want to give customers ability to update and delete orders?
  #   return update_preorder(preorder, request.data)
  # elif request.method == 'DELETE':
  #   return delete_preorder(preorder)
  
def get_preorder_details(preorder):
  serializer = Preorder2Serializer(preorder)
  return Response(serializer.data)

# def update_preorder(preorder, data): 
#   preorder_data = Preorder2Serializer(preorder, data=data, partial=True)
#   if preorder_data.is_valid():
#     preorder_data.save()
#     return Response(preorder_data.data)
#   return Response(status=status.HTTP_400_BAD_REQUEST)

# def delete_preorder(preorder): 
#   preorder.delete()
#   return Response({'message': "deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

