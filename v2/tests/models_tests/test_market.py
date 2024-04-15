from django.test import TestCase
from v2.models import Market

class MarketModelTest(TestCase):
  def setUp(self):
    self.market_data = {
        'market_name': 'Test Market',
        'location': 'Test Location',
        'details': 'Test Details',
        'start_date': '2023-01-01',
        'end_date': '2023-01-02'
    }

    self.market = Market.objects.create(**self.market_data)

  def test_market_model(self):
    market = Market.objects.get(id=self.market.id)
    
    self.assertEqual(market.market_name, self.market_data['market_name'])
    self.assertEqual(market.location, self.market_data['location'])
    self.assertEqual(market.details, self.market_data['details'])
    self.assertEqual(str(market.start_date), self.market_data['start_date'])
    self.assertEqual(str(market.end_date), self.market_data['end_date'])
    self.assertEqual(str(market), self.market_data['market_name'])
  