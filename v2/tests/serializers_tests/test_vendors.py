from django.test import TestCase
from v2.models import Vendor, Market
from v2.serializers import VendorSerializer

class VendorSerializerTest(TestCase):
  def setUp(self):
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

    self.serializer_data = {
      'id': self.vendor.id,
      'vendor_name': self.vendor.vendor_name,
      'first_name': self.vendor.first_name,
      'last_name': self.vendor.last_name,
      'phone': self.vendor.phone,
      'email': self.vendor.email,
      'password': self.vendor.password,
      'default_zipcode': self.vendor.default_zipcode,
      'date_created': self.vendor.date_created.isoformat(),
      'updated_at': self.vendor.updated_at.isoformat(),
    }

  def test_vendor_serializer(self):
    serializer = VendorSerializer(instance=self.vendor)
    self.assertEqual(serializer.data['vendor_name'], self.vendor_data['vendor_name'])
    self.assertEqual(serializer.data['first_name'], self.vendor_data['first_name'])
    self.assertEqual(serializer.data['email'], self.vendor_data['email'])

  def test_vendor_deserializer(self):
    serializer = VendorSerializer(data=self.serializer_data)
    self.assertTrue(serializer.is_valid())
    deserialized_data = serializer.validated_data
    self.assertEqual(deserialized_data['vendor_name'], self.vendor_data['vendor_name'])
    self.assertEqual(deserialized_data['first_name'], self.vendor_data['first_name'])
    self.assertEqual(deserialized_data['email'], self.vendor_data['email'])
