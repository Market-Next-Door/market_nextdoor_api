from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import VendorMarketSerializer
from ..models import Vendor, Market, VendorMarket

@api_view(['GET', 'POST'])
def vendor_market_list(request, vendor_id):
    try:
        check_vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return Response({"error": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_vendor_market_list(request, check_vendor)
    elif request.method == 'POST':
        return create_vendor_market(request)

def get_vendor_market_list(request, check_vendor):
    vendor_markets = VendorMarket.objects.filter(vendor=check_vendor)
    serializer = VendorMarketSerializer(vendor_markets, many=True)
    return Response(serializer.data)

def create_vendor_market(request):
    serializer = VendorMarketSerializer(data=request.data)
    if serializer.is_valid():
        vendor_id = serializer.validated_data['vendor']
        market_id = serializer.validated_data['market']

        if VendorMarket.objects.filter(vendor=vendor_id, market=market_id).exists():
            return Response({"error": "VendorMarket association already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_market_details(request, vendor_id, market_id):
    try:
        check_vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return Response({"error": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        check_market = Market.objects.get(pk=market_id)
    except Market.DoesNotExist:
        return Response({"error": "Market not found."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        check_vendor_market = VendorMarket.objects.get(vendor=check_vendor, market=check_market)
    except VendorMarket.DoesNotExist:
        return Response({"error": "VendorMarket not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_vendor_market(check_vendor_market)
    elif request.method == 'PUT':
        return update_vendor_market(check_vendor_market, request.data)
    elif request.method == 'DELETE':
        return delete_vendor_market(check_vendor_market)

def get_vendor_market(check_vendor_market):
    serializer = VendorMarketSerializer(check_vendor_market)
    return Response(serializer.data)

def update_vendor_market(check_vendor_market, data):
    serializer = VendorMarketSerializer(check_vendor_market, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

def delete_vendor_market(check_vendor_market):
    check_vendor_market.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)