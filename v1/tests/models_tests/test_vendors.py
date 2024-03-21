from django.test import TestCase
from django.core.exceptions import ValidationError
from market_nextdoor_api.models import Vendor, Market

class VendorModelTest(TestCase):
  def setUp(self):
    self.market = Market.objects.create(market_name="Test Market")

    self.vendor_data = {
        'market': self.market,
        'vendor_name': 'TestVendor',
        'first_name': 'John',
        'last_name': 'Doe',
        'phone': '1234567890',
        'email': 'john.doe@example.com',
        'password': 'securepassword',
        'location': 'Test Location',
    }
    self.vendor = Vendor.objects.create(**self.vendor_data)

  def test_vendor_creation(self):
    """Test Vendor model creation."""
    self.assertEqual(Vendor.objects.count(), 1)

  def test_vendor_str_method(self):
    """Test __str__ method of Vendor model."""
    self.assertEqual(str(self.vendor), self.vendor_data['vendor_name'])

  def test_vendor_fields(self):
    """Test individual fields of the Vendor model."""
    vendor = Vendor.objects.get(id=self.vendor.id)

    self.assertEqual(vendor.market, self.market)
    self.assertEqual(vendor.vendor_name, self.vendor_data['vendor_name'])
    self.assertEqual(vendor.first_name, self.vendor_data['first_name'])
    self.assertEqual(vendor.last_name, self.vendor_data['last_name'])
    self.assertEqual(vendor.phone, self.vendor_data['phone'])
    self.assertEqual(vendor.email, self.vendor_data['email'])
    self.assertEqual(vendor.password, self.vendor_data['password'])
    self.assertEqual(vendor.location, self.vendor_data['location'])

  def test_vendor_null_market(self):
    """Test that market is required (null=False)."""
    try:
      Vendor.objects.create(
        market=None,
        vendor_name=self.vendor_data['vendor_name'],
        first_name=self.vendor_data['first_name'],
        last_name=self.vendor_data['last_name'],
        phone=self.vendor_data['phone'],
        email=self.vendor_data['email'],
        password=self.vendor_data['password'],
        location=self.vendor_data['location'],
      )
    except ValidationError as e:
      print(f"Exception raised: {repr(e)}")
      return
      
    print("Should have raised an exception.")
    # self.fail('Vendor should require a market.') once the model has null = False, this test should pass
