from django.test import TestCase
from v2.models import Preorder, Vendor, Item, Customer, Market, VendorMarket, CustomerMarket
from v2.serializers import PreorderSerializer
import pdb

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
      'vendor_name': 'TestVendor',
      'first_name': 'John',
      'last_name': 'Doe',
      'phone': '1234567890',
      'email': 'john.doe@example.com',
      'password': 'securepassword',
      'default_zipcode': '80013',
      'date_created': '2023-01-01T00:00:00Z',  
      'updated_at': '2023-01-02T00:00:00Z',  
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
      'image': 'Test Image',
    }

    self.item = Item.objects.create(**self.item_data)

    self.customer_data = {
      'first_name': 'John',
      'last_name': 'Doe',
      'phone': '1234567890',
      'email': 'test2@abc.com',
      'password': 'securepassword',
      'default_zipcode': '80013',
      'date_created': '2023-01-01T00:00:00Z',
      'updated_at': '2023-01-02T00:00:00Z',
    }

    self.customer = Customer.objects.create(**self.customer_data)

    self.customer_market = CustomerMarket.objects.create(customer=self.customer, market=self.market)

    self.preorder_data = {
      'customer': self.customer,
      'item': self.item,
      'quantity_requested': 1,
      'ready': False,
      'packed': False,
      'fulfilled': False,
      'date_created': '2023-01-01T00:00:00Z',
      'updated_at': '2023-01-02T00:00:00Z',
    }

    self.preorder = Preorder.objects.create(**self.preorder_data)

    self.serializer_data = {
      'id': self.preorder.id,
      'item': self.preorder.item.id,
      'customer': self.preorder.customer.id,
      'quantity_requested': self.preorder.quantity_requested,
      'ready': self.preorder.ready,
      'packed': self.preorder.packed,
      'fulfilled': self.preorder.fulfilled,
      'date_created': self.preorder.date_created.isoformat(),
      'updated_at': self.preorder.updated_at.isoformat(),
    }

  def test_preorder_serializer(self):
    serializer = PreorderSerializer(instance=self.preorder)
    self.assertEqual(serializer.data['item'], self.preorder_data['item'].id)
    self.assertEqual(serializer.data['customer'], self.preorder_data['customer'].id)
    self.assertEqual(serializer.data['quantity_requested'], self.preorder_data['quantity_requested'])
    self.assertEqual(serializer.data['ready'], self.preorder_data['ready'])
    self.assertEqual(serializer.data['packed'], self.preorder_data['packed'])
    self.assertEqual(serializer.data['fulfilled'], self.preorder_data['fulfilled'])

  def test_preorder_deserializer(self):
    serializer = PreorderSerializer(data=self.serializer_data)
    self.assertTrue(serializer.is_valid())
    deserialized_data = serializer.validated_data
    self.assertEqual(deserialized_data['item'], self.preorder_data['item'])
    self.assertEqual(deserialized_data['customer'], self.preorder_data['customer'])
    self.assertEqual(deserialized_data['quantity_requested'], self.preorder_data['quantity_requested'])
    self.assertEqual(deserialized_data['ready'], self.preorder_data['ready'])
    self.assertEqual(deserialized_data['packed'], self.preorder_data['packed'])
    self.assertEqual(deserialized_data['fulfilled'], self.preorder_data['fulfilled'])
