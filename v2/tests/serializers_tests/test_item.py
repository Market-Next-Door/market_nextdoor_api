from django.test import TestCase
from v2.models import Vendor, Item, Customer, Market, VendorMarket, CustomerMarket
from v2.serializers import ItemSerializer
import pdb

class ItemSerializerTest(TestCase):
    def setUp(self):
        self.market_data = {
            'market_name': 'Test Market',
            'location': 'Test Location',
            'details': 'Test Details',
            'start_date': '2023-01-01',  
            'end_date': '2023-01-02',  
            'date_created': '2023-01-01T00:00:00Z',  
            'updated_at': '2023-01-02T00:00:00Z',  
        }

        self.market = Market.objects.create(**self.market_data)

        self.vendor_data = {
            'vendor_name': 'TestVendor',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'email': 'john.doe@example.com',
            'password': 'securepassword',
            'location': 'Test Location',
            'date_created': '2023-01-01T00:00:00Z',  
            'updated_at': '2023-01-02T00:00:00Z'
        }

        self.vendor = Vendor.objects.create(**self.vendor_data)

        self.vendor_market = VendorMarket.objects.create(vendor=self.vendor, market=self.market)

        self.item_data = {
            'item_name': 'Test Item',
            'vendor': self.vendor,
            'price': 10.00,
            'size': 'Test Size',
            'quantity': 1,
            'availability': True,
            'description': 'Test Description',
            'date_created': '2023-01-01T00:00:00Z',
            'updated_at': '2023-01-02T00:00:00Z',
            'image': None
        }

        self.item = Item.objects.create(**self.item_data)

    def test_item_serializer(self):
        serializer = ItemSerializer(instance=self.item)
        serialized_price = float(serializer.data['price'])
        self.assertEqual(serializer.data['item_name'], self.item_data['item_name'])
        self.assertEqual(serializer.data['vendor'], self.item_data['vendor'].id)
        self.assertEqual(serialized_price, self.item_data['price'])
        self.assertEqual(serializer.data['quantity'], self.item_data['quantity'])
        self.assertEqual(serializer.data['description'], self.item_data['description'])
        self.assertEqual(serializer.data['image'], self.item_data['image'])
