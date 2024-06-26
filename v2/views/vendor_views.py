from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import VendorSerializer, PreorderSerializer
from ..models import Vendor, Preorder, Market, VendorMarket
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


# Vendor by Market
@api_view(['GET', 'POST'])
def vendors_by_market_list(request, market_id):
  # Input validation
  if not (isinstance(market_id, int) and market_id > 0):
    return Response({"error": "Invalid market id."}, status=status.HTTP_400_BAD_REQUEST)
  
  market = get_market_object(market_id)

  if request.method == 'GET':
    return get_vendors_by_market_list(request, market)
  elif request.method == 'POST':
    return create_vendor_market(request, market)

def get_market_object(market_id):
  try:
    return Market.objects.get(pk=market_id)
  except Market.DoesNotExist:
    return Response({"error": "Market not found."}, status=status.HTTP_404_NOT_FOUND)

def get_vendors_by_market_list(request, market):
  vendors = market.vendors.all()
  serializer = VendorSerializer(vendors, many=True)
  return Response(serializer.data)

def create_vendor_market(request, market):
  vendor_id = request.data["id"]
  if (isinstance(vendor_id, int) and vendor_id > 0):

    try:
      vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
      return Response({"error": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)

    if VendorMarket.objects.filter(vendor=vendor, market=market).exists():
      return Response({"error": "Vendor is already associated with the market."}, status=status.HTTP_400_BAD_REQUEST)

    VendorMarket.objects.create(vendor=vendor, market=market)

    return Response({"message": "Vendor was associated successfully."}, status=status.HTTP_201_CREATED)
  return Response({"error": "Vendor ID is invalid."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def vendor_by_market_details(request, vendor_id, market_id):
  # Input validation
  if not (isinstance(market_id, int) and market_id > 0):
    return Response({"error": "Invalid market id."}, status=status.HTTP_400_BAD_REQUEST)
  if not (isinstance(vendor_id, int) and vendor_id > 0):
    return Response({"error": "Invalid vendor id."}, status=status.HTTP_400_BAD_REQUEST)

  market = get_market_object(market_id)
  vendor = get_vendor_object(vendor_id)

  if request.method == 'GET':
    return get_vendor_by_market_details(vendor)
  elif request.method == 'DELETE':
    return delete_vendor_market(market, vendor)

def get_market_object(market_id):
  try:
    return Market.objects.get(pk=market_id)
  except Market.DoesNotExist:
    return Response({"error": "Market not found."}, status=status.HTTP_404_NOT_FOUND)

def get_vendor_object(vendor_id):
  try:
    return Vendor.objects.get(pk=vendor_id)
  except Vendor.DoesNotExist:
    return Response({"error": "vendor not found."}, status=status.HTTP_404_NOT_FOUND)

def get_vendor_by_market_details(vendor):
  serializer = VendorSerializer(vendor)
  return Response(serializer.data)

def delete_vendor_market(market, vendor):
  # pdb.set_trace()
  vendor_market = VendorMarket.objects.filter(vendor=vendor, market=market)
  vendor_market.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)


# Vendor Preorders
@api_view(['GET'])
def preorder_by_vendor_list(request, market_id, vendor_id):
  # Input validation
  if not (isinstance(market_id, int) and market_id > 0):
    return Response({"error": "Invalid market id."}, status=status.HTTP_400_BAD_REQUEST)
  if not (isinstance(vendor_id, int) and vendor_id > 0):
    return Response({"error": "Invalid vendor id."}, status=status.HTTP_400_BAD_REQUEST)
  
  try:
    market = Market.objects.get(pk=market_id)
  except Market.DoesNotExist:
    return Response({"error": "Market not found."}, status=status.HTTP_404_NOT_FOUND)
  try:
    vendor = market.vendors.get(pk=vendor_id)
  except Vendor.DoesNotExist:
    return Response({"error": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)

  preorders = Preorder.objects.filter(item__vendor=vendor)
  serializer = PreorderSerializer(preorders, many=True)
  return Response(serializer.data)

@api_view(['GET', 'PUT'])
def preorder_by_vendor_details(request, market_id, vendor_id, preorder_id):
  # Input validation
  if not (isinstance(market_id, int) and market_id > 0):
    return Response({"error": "Invalid market id."}, status=status.HTTP_400_BAD_REQUEST)
  if not (isinstance(vendor_id, int) and vendor_id > 0):
    return Response({"error": "Invalid vendor id."}, status=status.HTTP_400_BAD_REQUEST)
  
  try:
    market = Market.objects.get(pk=market_id)
  except Market.DoesNotExist:
    return Response({"error": "Market not found."}, status=status.HTTP_404_NOT_FOUND)
  try:
    vendor = market.vendors.get(pk=vendor_id)
  except Vendor.DoesNotExist:
    return Response({"error": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
  try:
    preorder = Preorder.objects.get(pk=preorder_id, item__vendor=vendor)
  except Preorder.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    return get_preorder_vendor_list_details(preorder)
  elif request.method == 'PUT':
    return update_preorder(preorder, request.data)

def get_preorder_vendor_list_details(preorder):
  serializer = PreorderSerializer(preorder)
  return Response(serializer.data, status=status.HTTP_200_OK)

def update_preorder(preorder, data):
  preorder_data = PreorderSerializer(preorder, data=data, partial=True)
  if preorder_data.is_valid():
    preorder_data.save()
    return Response(preorder_data.data)
  return Response(status=status.HTTP_400_BAD_REQUEST) 
