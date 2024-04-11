from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import CustomerMarketSerializer
from ..models import Customer, Market, CustomerMarket
import pdb

@api_view(['GET', 'POST'])
def customer_market_list(request, customer_id):
    try:
        check_customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_customer_market_list(request, check_customer)
    elif request.method == 'POST':
        return create_customer_market(request)

def get_customer_market_list(request, check_customer):
    customer_markets = CustomerMarket.objects.filter(customer=check_customer)
    serializer = CustomerMarketSerializer(customer_markets, many=True)
    return Response(serializer.data)

def create_customer_market(request):
    serializer = CustomerMarketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "CustomerMarket association created."}, serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def customer_market_details(request, customer_id, market_id):
    try:
        check_customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        check_market = Market.objects.get(pk=market_id)
    except Market.DoesNotExist:
        return Response({"error": "Market not found."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        check_customer_market = CustomerMarket.objects.get(customer=check_customer, market=check_market)
    except CustomerMarket.DoesNotExist:
        return Response({"error": "CustomerMarket not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return get_customer_market(check_customer_market)
    elif request.method == 'DELETE':
        return delete_customer_market(check_customer_market)

def get_customer_market(check_customer_market):
    serializer = CustomerMarketSerializer(check_customer_market)
    return Response(serializer.data)

def delete_customer_market(check_customer_market):
    check_customer_market.delete()
    return Response({"message": "CustomerMarket association was deleted."}, status=status.HTTP_204_NO_CONTENT)