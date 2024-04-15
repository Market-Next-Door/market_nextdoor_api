from rest_framework.test import APITestCase
from django.test import TestCase
from v2.models import *
import pdb

class CustomerMarketModelTest(TestCase):
  def setUp(self):
    self.customer = Customer.objects.create(
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
    self.customer_market = CustomerMarket.objects.create(
       customer = self.customer,
       market = self.market
    )

  def test_model_fields(self):
      customer_market = CustomerMarket.objects.get(customer=self.customer, market=self.market)
      # Test the values of the fields
      self.assertEqual(customer_market.customer, self.customer)
      self.assertEqual(customer_market.market, self.market)

