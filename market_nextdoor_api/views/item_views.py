from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ItemSerializer, VendorSerializer
from ..models import Item, Vendor


# Item CRUD functions (SRP)
@api_view(['GET', 'POST'])
def item_list(request, vendor_id):
  try:
    check_vendor = Vendor.objects.get(pk=vendor_id)
  except Vendor.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    return get_item_list(request, check_vendor)
  elif request.method == 'POST':
    return create_item(request)

def get_item_list(request, check_vendor):
  items = Item.objects.filter(vendor=check_vendor)
  serializer = ItemSerializer(items, many=True)
  return Response(serializer.data)

def create_item(request):
  serializer = ItemSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_details(request, vendor_id, item_id):
  try:
    vendor = Vendor.objects.get(pk=vendor_id)
  except Vendor.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  try:
    item = Item.objects.get(pk=item_id, vendor=vendor)
  except Item.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_item_details(item)
  elif request.method == 'PUT':
    return update_item(item, request.data)
  elif request.method == 'DELETE':
    return delete_item(item)
  
def get_item_details(item):
  serializer = ItemSerializer(item)
  return Response(serializer.data)

def update_item(item, data):
  item_data = ItemSerializer(item, data=data, partial=True)
  if item_data.is_valid():
    item_data.save()
    return Response(item_data.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_item(item):
  item.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

