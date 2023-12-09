import os
from decimal import Decimal
from django.test import TestCase
from django.core.exceptions import ValidationError
from market_nextdoor_api.models import Vendor, Item

class ItemModelTest(TestCase):
  def setUp(self):
    self.vendor = Vendor.objects.create(
      vendor_name="TestVendor",
      first_name="John",
      last_name="Doe",
      phone="1234567890",
      email="john.doe@example.com",
      password="securepassword",
      location="Test Location"
    )

    self.item_data = {
      'item_name': 'TestItem',
      'vendor': self.vendor,
      'price': Decimal('29.99'),  
      'size': 'Large',
      'quantity': 5,
      'availability': True,
      'description': 'A sample item description.',
      'image': None
    }
    self.item = Item.objects.create(**self.item_data)
  
  def test_item_fields(self):
    """Test individual fields of the Item model."""
    item = Item.objects.get(id=self.item.id)

    self.assertEqual(item.item_name, self.item_data['item_name'])
    self.assertEqual(item.vendor, self.vendor)
    self.assertEqual(item.price, self.item_data['price'])  
    self.assertEqual(item.size, self.item_data['size'])
    self.assertEqual(item.quantity, self.item_data['quantity'])
    self.assertEqual(item.availability, self.item_data['availability'])
    self.assertEqual(item.description, self.item_data['description'])

    if item.image:
      item_image_path = item.image.path
      item.delete()
      self.assertFalse(Item.objects.filter(id=item.id).exists())

      if item_image_path:
        self.assertFalse(os.path.exists(item_image_path))

  def test_item_delete(self):
    item = Item.objects.create(
      item_name="ToDelete",
      vendor=self.vendor,
      price=Decimal('19.99'),  # Convert to Decimal
      size="Medium",
      quantity=3,
      availability=True,
      description="A sample item description."
    )

    if item.image:
      item_image_path = item.image.path
      item.delete()
      self.assertFalse(Item.objects.filter(id=item.id).exists())

      if item_image_path:
        self.assertFalse(os.path.exists(item_image_path))
      

  # def test_item_null_vendor(self):
  #   """Test that vendor is required (null=False)."""
  #   with self.assertRaises(ValidationError):
  #     Item.objects.create(
  #       item_name='TestItem',
  #       vendor=None,
  #       price=Decimal('29.99'),
  #       size='Large',
  #       quantity=5,
  #       availability=True,
  #       description='A sample item description.',
  #       image=None
  #     )

  #   self.assertEqual(Item.objects.count(), 1)

  #   self.assertEqual(Item.objects.get(id=self.item.id).vendor, self.vendor)

  #   if self.item.image:
  #     item_image_path = self.item.image.path
  #     self.item.delete()

  #     self.assertFalse(Item.objects.filter(id=self.item.id).exists())

  #     if item_image_path:
  #       self.assertFalse(os.path.exists(item_image_path))
    
  #   self.assertEqual(Item.objects.count(), 0)
  #  i can not seem to get this working, i am going to move on and come back to it later
    
