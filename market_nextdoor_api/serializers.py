from rest_framework import serializers
from .models import *
import pdb


# Customers
class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'password', 'location', 'date_created', 'updated_at']

# Vendors
class VendorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vendor
    fields = ['id', 'market', 'vendor_name', 'first_name', 'last_name', 'phone', 'email', 'password', 'location', 'date_created', 'updated_at']

# Items
class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = ['id', 'item_name', 'vendor', 'price', 'size', 'quantity', 'availability', 'description', 'image', 'date_created', 'updated_at']

# Markets
class MarketSerializer(serializers.ModelSerializer):
  class Meta:
    model = Market
    fields = ['id', 'market_name', 'location', 'details', 'start_date', 'end_date', 'date_created', 'updated_at']

# Preorders
class PreorderSerializer(serializers.ModelSerializer):
  vendor_id = serializers.SerializerMethodField()

  class Meta:
    model = Preorder
    fields = ['id', 'customer', 'item', 'packed', 'fulfilled', 'ready', 'quantity_requested', 'vendor_id', 'date_created', 'updated_at', ]

  def get_vendor_id(self, obj):
    return obj.item.vendor_id 