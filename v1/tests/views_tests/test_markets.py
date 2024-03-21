from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ...models import *
import pdb

class MarketTestCase(APITestCase):
  def setUp(self):
    self.market1 = Market.objects.create(
      market_name="Saturday Market",
      location="Denver, TX",
      details="This Saturday only!",
      start_date="2023-12-06",
      end_date="2023-12-07"
    )

# GET (index) request test
  def test_market_list(self):
    url = reverse('market_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code,status.HTTP_200_OK)
    self.assertEqual(response.data[0]["id"], self.market1.id)
    self.assertEqual(response.data[0]["market_name"], self.market1.market_name)
    self.assertEqual(response.data[0]["location"], self.market1.location)
    self.assertEqual(response.data[0]["details"], self.market1.details)
    self.assertEqual(response.data[0]["start_date"], self.market1.start_date)
    self.assertEqual(response.data[0]["end_date"], self.market1.end_date)

# POST request test
  def test_post_market(self):
    url = reverse('market_list')
    data = {
      'market_name': "Sunday Market", 
      'location': "Austin, TX", 
      'details': "THIS SUNDAY SUNDAY SUNDAY!!!", 
      'start_date': "2023-12-07", 
      'end_date': "2023-12-07"
    }
    response = self.client.post(url, data)
    new_market = Market.objects.last()
    self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    self.assertEqual(Market.objects.count(), 2)
    self.assertEqual(response.data["id"], new_market.id)
    self.assertEqual(response.data["market_name"], new_market.market_name)
    self.assertEqual(response.data["location"], new_market.location)
    self.assertEqual(response.data["details"], new_market.details)
    self.assertEqual(response.data["start_date"], "2023-12-07")
    self.assertEqual(response.data["end_date"], "2023-12-07")

# GET (show) request test
  def test_market_details(self):
    url = reverse('market_details', args=[self.market1.pk])
    response = self.client.get(url)
    self.assertEqual(response.status_code,status.HTTP_200_OK)
    self.assertEqual(response.data["id"], self.market1.id)
    self.assertEqual(response.data["market_name"], self.market1.market_name)
    self.assertEqual(response.data["location"], self.market1.location)
    self.assertEqual(response.data["details"], self.market1.details)
    self.assertEqual(response.data["start_date"], self.market1.start_date)
    self.assertEqual(response.data["end_date"], self.market1.end_date)

# PUT request test
  def test_update_market(self):
    url = reverse('market_details', args=[self.market1.pk])
    data = {
      'market_name': "Sunday Market", 
      'location': "Austin, TX", 
      'details': "ALL WEEKEND LONG!!!", 
      'start_date': "2023-12-07", 
      'end_date': "2023-12-08"
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code,status.HTTP_200_OK)
    self.assertEqual(response.data["id"], self.market1.id)
    self.assertEqual(response.data["market_name"], "Sunday Market")
    self.assertEqual(response.data["location"], "Austin, TX")
    self.assertEqual(response.data["details"], "ALL WEEKEND LONG!!!")
    self.assertEqual(response.data["start_date"], "2023-12-07")
    self.assertEqual(response.data["end_date"], "2023-12-08")

# DELETE request test
  def test_delete_market(self):
    self.assertEqual(Market.objects.count(), 1)
    url = reverse('market_details', args=[self.market1.pk])
    response = self.client.delete(url)
    self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT )
    self.assertEqual(Market.objects.count(), 0)
