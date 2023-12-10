from django.test import TestCase
from market_nextdoor_api.models import Preorder, Vendor, Item, Customer
from market_nextdoor_api.serializers import PreorderSerializer

class PreorderSerializerTest(TestCase):
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
      'market': self.market,
      'vendor_name': 'TestVendor',
      'first_name': 'John',
      'last_name': 'Doe',
      'phone': '1234567890',
      'email': 'john.doe@example.com',
      'password': 'securepassword',
      'location': 'Test Location',
      'date_created': '2023-01-01T00:00:00Z',  
      'updated_at': '2023-01-02T00:00:00Z',  
    }

    self.vendor = Vendor.objects.create(**self.vendor_data)

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
      'image': 'Test Image',
    }

    self.vendor = Vendor.objects.create(**self.vendor_data)

    self.customer_data = {
      'first_name': 'John',
      'last_name': 'Doe',
      'phone': '1234567890',
      'email': 'test2@abc.com',
      'password': 'securepassword',
      'location': 'Test Location',
      'date_created': '2023-01-01T00:00:00Z',
      'updated_at': '2023-01-02T00:00:00Z',
    }

    self.customer = Customer.objects.create(**self.customer_data)

    self.preorder_data = {
      'vendor_id': self.vendor.id,
      'item_id': self.item.id,
      'customer_id': self.customer.id,
      'quantity_requested': 1,
      'ready': False,
      'date_created': '2023-01-01T00:00:00Z',
      'updated_at': '2023-01-02T00:00:00Z',
    }

    self.preorder = Preorder.objects.create(**self.preorder_data)

    self.serializer_data = {
      'vendor_id': self.preorder.vendor.id,
      'item_id': self.preorder.item.id,
      'customer_id': self.preorder.customer.id,
      'quantity_requested': self.preorder.quantity_requested,
      'ready': self.preorder.ready,
      'date_created': self.preorder.date_created.isoformat(),
      'updated_at': self.preorder.updated_at.isoformat(),
    }

  def test_preorder_serializer(self):
    serializer = PreorderSerializer(instance=self.preorder)
    self.assertEqual(serializer.data, self.serializer_data)
    self.assertEqual(serializer.data['vendor_id'], self.preorder_data['vendor_id'])
    self.assertEqual(serializer.data['item_id'], self.preorder_data['item_id'])
    self.assertEqual(serializer.data['customer_id'], self.preorder_data['customer_id'])
    self.assertEqual(serializer.data['quantity_requested'], self.preorder_data['quantity_requested'])
    self.assertEqual(serializer.data['ready'], self.preorder_data['ready'])
