from django.test import TestCase
from v2.models import Market
from datetime import date

class MarketModelTests(TestCase):

  def setUp(self):
    self.market = Market.objects.create(
      market_name='Test Market',
      location='Test Location',
      details='Test Details',
      start_date=date(2023, 1, 1),
      end_date=date(2023, 12, 31)
    )

  def test_market_attributes(self):
    self.assertEqual(str(self.market), 'Test Market')
    self.assertEqual(self.market.start_date, date(2023, 1, 1))
    self.assertEqual(self.market.end_date, date(2023, 12, 31))
