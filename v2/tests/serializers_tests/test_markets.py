from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from v2.models import Market
from v2.serializers import MarketSerializer
from datetime import date

class MarketSerializerTests(APITestCase):

  def setUp(self):
    self.market_data = {
      'market_name': 'Test Market',
      'location': 'Test Location',
      'details': 'Test Details',
      'start_date': date(2023, 1, 1),
      'end_date': date(2023, 12, 31)
    }
    self.market = Market.objects.create(**self.market_data)

  def test_serialize_market(self):
    """Test if the serializer can serialize a Market instance."""
    serializer = MarketSerializer(instance=self.market)
    expected_data = {
      'id': self.market.id,
      'market_name': 'Test Market',
      'location': 'Test Location',
      'details': 'Test Details',
      'start_date': '2023-01-01',
      'end_date': '2023-12-31',
      'date_created': self.market.date_created.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
      'updated_at': self.market.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    }
    self.assertEqual(serializer.data, expected_data)

  def test_deserialize_market(self):
    """Test if the serializer can deserialize valid data."""
    serializer = MarketSerializer(data=self.market_data)
    self.assertTrue(serializer.is_valid())
    self.assertEqual(serializer.validated_data['market_name'], 'Test Market')

  def test_invalid_data(self):
    """Test if the serializer handles invalid data."""
    invalid_data = {
      'market_name': '',
      'location': 'Test Location',
      'details': 'Test Details',
      'start_date': date(2023, 1, 1),
      'end_date': date(2023, 12, 31)
    }
    serializer = MarketSerializer(data=invalid_data)
    self.assertFalse(serializer.is_valid())

  def test_serializer_with_request(self):
    """Test using the serializer in a view with request data."""
    request_data = {
      'market_name': 'Updated Market Name',
      'location': 'Updated Location',
      'details': 'Updated Details',
      'start_date': '2023-01-01',
      'end_date': '2023-12-31',
    }
    serializer = MarketSerializer(instance=self.market, data=request_data, partial=True)
    self.assertTrue(serializer.is_valid())
    serializer.save()
    self.market.refresh_from_db()
    self.assertEqual(self.market.market_name, 'Updated Market Name')

  def test_serializer_validation_error_response(self):
    """Test if the serializer returns validation errors in the response."""
    invalid_data = {
      'market_name': '',
      'location': 'Test Location',
      'details': 'Test Details',
      'start_date': date(2023, 1, 1),
      'end_date': date(2023, 12, 31)
    }
    response = self.client.post(reverse('market_list'), invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertIn('market_name', response.data) 