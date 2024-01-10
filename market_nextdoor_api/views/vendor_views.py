from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import VendorSerializer, PreorderSerializer, Preorder_testSerializer
from ..models import Vendor, Preorder, Preorder_test, Preorder_testItem, Item
import pdb


@api_view(['GET', 'POST'])
def vendor_list(request):
  if request.method == 'GET':
    return get_vendor_list(request)
  elif request.method == 'POST':
    return create_vendor(request)

def get_vendor_list(request):
  vendors = Vendor.objects.all()
  serializer = VendorSerializer(vendors, many=True)
  return Response(serializer.data)

def create_vendor(request):
  serializer = VendorSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_details(request, vendor_id):
  vendor = get_vendor_object(vendor_id)
  
  if request.method == 'GET':
    return get_vendor_details(vendor)
  elif request.method == 'PUT':
    return update_vendor(vendor, request.data)
  elif request.method == 'DELETE':
    return delete_vendor(vendor)

def get_vendor_object(vendor_id):
  try:
    return Vendor.objects.get(pk=vendor_id)
  except Vendor.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

def get_vendor_details(vendor):
  serializer = VendorSerializer(vendor)
  return Response(serializer.data)

def update_vendor(vendor, data):
  vendor_data = VendorSerializer(vendor, data=data, partial=True)
  if vendor_data.is_valid():
    vendor_data.save()
    return Response(vendor_data.data)
  return Response(vendor_data.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_vendor(vendor):
  vendor.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)



# Preorder CRUD functions - Vendor list (SRP)
@api_view(['GET'])
def preorder_vendor_list(request, vendor_id):
  try:
    check_vendor = Vendor.objects.get(pk=vendor_id)
  except Vendor.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    return get_preorder_vendor_list(request, check_vendor)


def get_preorder_vendor_list(request, check_vendor):
  preorders = Preorder.objects.filter(item__vendor=check_vendor)
  serializer = PreorderSerializer(preorders, many=True)
  return Response(serializer.data)

@api_view(['GET', 'PUT'])
def preorder_vendor_list_details(request, vendor_id, preorder_id):
  try:
    check_vendor = Vendor.objects.get(pk=vendor_id)
  except Vendor.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  try:
    preorder = Preorder.objects.get(pk=preorder_id, item__vendor=check_vendor)
  except Preorder.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_preorder_vendor_list_details(preorder)
  elif request.method == 'PUT':
    return update_preorder(preorder, request.data)
  elif request.method == 'DELETE':
    return delete_preorder(preorder)
  
def get_preorder_vendor_list_details(preorder):
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
  preorder_tests = Preorder_test.objects.filter(items__vendor=check_vendor).distinct()

  serializer = Preorder_testSerializer(preorder_tests, many=True)
  return Response(serializer.data)

def create_preorder_test(request, check_vendor):
  serializer = Preorder_testSerializer(data=request.data)
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
      Preorder_testItem.objects.create(
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
    preorder = Preorder_test.objects.get(pk=preorder_id)
  except preorder.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_preorder_details(preorder, vendor)
  elif request.method == 'PUT':
    return update_preorder(preorder, request.data)
  elif request.method == 'DELETE':
    return delete_preorder(preorder)
  
def get_preorder_details(preorder, vendor):
  items = Preorder_testItem.objects.filter(preorder=preorder, item__vendor=vendor)
  if not items.exists():
    return Response({"error": f'Preorder {preorder.id} does not have associated items with vendor {vendor.id}'}, 
          status=status.HTTP_400_BAD_REQUEST)
  serializer = Preorder_testSerializer(preorder)
  return Response(serializer.data)

def update_preorder(preorder, data):
  preorder_data = Preorder_testSerializer(preorder, data=data, partial=True)
  if preorder_data.is_valid():
    preorder_data.save()
    return Response(preorder_data.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_preorder(preorder): 
  preorder.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)
