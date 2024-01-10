from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import PreorderSerializer, CustomerSerializer, Preorder2Serializer
from ..models import Preorder, Customer, Preorder2, Preorder2Item, Item, Vendor
import pdb


#manytomany views testing
@api_view(['GET', 'POST'])
def preorder_test_list(request, vendor_id):
  try:
    check_vendor = Vendor.objects.get(pk=vendor_id)
  except Vendor.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    return get_preorder_test_list(request, check_vendor)
  elif request.method == 'POST':
    return create_preorder_test(request, check_vendor)

def get_preorder_test_list(request, check_vendor):
  preorder_tests = Preorder2.objects.filter(items__vendor=check_vendor).distinct()

  serializer = Preorder2Serializer(preorder_tests, many=True)
  return Response(serializer.data)

def create_preorder_test(request, check_vendor):
  serializer = Preorder2Serializer(data=request.data)
  if serializer.is_valid():
    preorder = serializer.save()
    response = preorder_item_helper(request, preorder, check_vendor, serializer)
    return response
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
def preorder_item_helper(request, preorder, check_vendor, serializer):
  items = request.data.get('items', [])
  for item_data in items:
    try:
      item = Item.objects.get(pk=item_data["item"])
    except Item.DoesNotExist:
      return Response({"error":f'Item {item_data["item"]} does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if item.vendor == check_vendor:
      Preorder2Item.objects.create(
        preorder=preorder,
        item_id=item.id,
        quantity_requested=item_data['quantity']
        )
    else:
      return Response({"error":f'Item with ID {item.id} does not belong to vendor {check_vendor.id}'},
                      status=status.HTTP_400_BAD_REQUEST)
  return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def preorder_test_details(request, vendor_id, preorder_id):
  try:
    vendor = Vendor.objects.get(pk=vendor_id)
  except vendor.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  try:
    preorder = Preorder2.objects.get(pk=preorder_id)
  except preorder.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_preorder_details(preorder, vendor)
  elif request.method == 'PUT':
    return update_preorder(preorder, request.data)
  elif request.method == 'DELETE':
    return delete_preorder(preorder)
  
def get_preorder_details(preorder, vendor):
  items = Preorder2Item.objects.filter(preorder=preorder, item__vendor=vendor)
  if not items.exists():
    return Response({"error": f'Preorder {preorder.id} does not have associated items with vendor {vendor.id}'}, 
          status=status.HTTP_400_BAD_REQUEST)
  serializer = Preorder2Serializer(preorder)
  return Response(serializer.data)

def update_preorder(preorder, data):
  preorder_data = Preorder2Serializer(preorder, data=data, partial=True)
  if preorder_data.is_valid():
    preorder_data.save()
    return Response(preorder_data.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_preorder(preorder): 
  preorder.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)
