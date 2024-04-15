from rest_framework.test import APITestCase
from django.test import TestCase
from v2.models import *
import pdb

class VendorMarketModelTest(TestCase):
  def setUp(self):
    self.vendor = Vendor.objects.create(
        first_name="George",
        last_name="Harrison",
        phone="1111111111",
        email="gh@gmail.com",
        default_zipcode="80013"
    )
    self.market = Market.objects.create(
        market_name="Saturday Market",
        location="Denver, Co"
    )
    self.vendor_market = VendorMarket.objects.create(
       vendor = self.vendor,
       market = self.market
    )

  def test_model_fields(self):
      vendor_market = VendorMarket.objects.get(vendor=self.vendor, market=self.market)
      # Test the values of the fields
      self.assertEqual(vendor_market.vendor, self.vendor)
      self.assertEqual(vendor_market.market, self.market)
      self.assertEqual(vendor_market.active, True)


