from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import VendorSerializer, PreorderSerializer
from ..models import Vendor, Preorder


@api_view(['GET', 'POST'])
def vendor_list(request):
  if request.method == 'GET':
    return get_vendor_list(request)
  elif request.method == 'POST':
    return create_vendor(request)

# GET (index) Request
def get_vendor_list(request):
  vendors = Vendor.objects.all()
  serializer = VendorSerializer(vendors, many=True)
  return Response(serializer.data)

# POST Request
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

# GET (show) Request
def get_vendor_details(vendor):
  serializer = VendorSerializer(vendor)
  return Response(serializer.data)

# PUT / UPDATE Request
def update_vendor(vendor, data):
  vendor_data = VendorSerializer(vendor, data=data, partial=True)
  if vendor_data.is_valid():
    vendor_data.save()
    return Response(vendor_data.data)
  return Response(vendor_data.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE Request
def delete_vendor(vendor):
  vendor.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)


###
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