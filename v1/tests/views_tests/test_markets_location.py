from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
import responses
import os
import pdb

class MarketLocationsTestCase(APITestCase):
  def setUp(self):
    self.usda_api_url = "https://www.usdalocalfoodportal.com/api/farmersmarket/"
    self.zipcode = 84106
    self.radius = 10
    self.endpoint = reverse('get_market_locations', args=[self.zipcode, self.radius])
  @responses.activate
  #This utilizes the new library above to mock environment variables like the API key for USDA
  @patch.dict('os.environ', {'USDA_API_KEY': 'f@kekey123'})

  #Happy path testing
  def test_get_market_locations_succesful_response(self):
    mock_response = {
    "data": [
        {
            "directory_type": "farmersmarket",
            "directory_name": "farmers market",
            "updatetime": "Mar 20th, 2023",
            "listing_image": "default-farmersmarket-4-3.jpg",
            "listing_id": "309131",
            "listing_name": "Union Station Farmers Market",
            "listing_desc": "null",
            "brief_desc": "",
            "mydesc": "",
            "contact_name": "null",
            "contact_email": "community@bcfm.org",
            "contact_phone": "800-872-7245",
            "media_website": "www.bcfm.org/union-station-farmers-marke",
            "media_facebook": "facebook.com/BoulderCountyFarmersMarkets",
            "media_twitter": "null",
            "media_instagram": "null",
            "media_pinterest": "null",
            "media_youtube": "null",
            "media_blog": "null",
            "location_address": "Union Station Farmers Market, 1701 Wynkoop St., Denver, CO 80202",
            "location_state": "Colorado",
            "location_city": "Denver",
            "location_street": "1701 Wynkoop St.",
            "location_zipcode": "80202",
            "location_x": "-104.99983322503695",
            "location_y": "39.75278314431321",
            "distance": "0.13159076759891786",
            "term": ""
        },
        {
            "directory_type": "farmersmarket",
            "directory_name": "farmers market",
            "updatetime": "Mar 20th, 2023",
            "listing_image": "default-farmersmarket-4-3.jpg",
            "listing_id": "309132",
            "listing_name": "Urban Farmers' Market",
            "listing_desc": "null",
            "brief_desc": "",
            "mydesc": "",
            "contact_name": "null",
            "contact_email": "Email not found",
            "contact_phone": "720-272-7467",
            "media_website": "http://urbanmarketdenver.com/",
            "media_facebook": "",
            "media_twitter": "null",
            "media_instagram": "null",
            "media_pinterest": "null",
            "media_youtube": "null",
            "media_blog": "null",
            "location_address": "16th St. Mall and Arapahoe, Skyline Park, Denver, CO, 80202",
            "location_state": "Colorado",
            "location_city": "Denver",
            "location_street": "16th St. Mall and Arapahoe",
            "location_zipcode": "80202",
            "location_x": "-104.99566998565368",
            "location_y": "39.747849996084284",
            "distance": "0.299144076737284",
            "term": ""
        }
      ]
    }
    #This utilizes the new library 'responses' to mock a response
    responses.add(responses.GET, f'{self.usda_api_url}?apikey={os.environ.get("USDA_API_KEY")}&zip={self.zipcode}&radius={self.radius}', json=mock_response, status=200)

    response = self.client.get(self.endpoint)
    response_data = response.json()
    #testing the response keys once parsed by the method
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIn('market_name', response_data[0])
    self.assertIn('listing_id', response_data[0])
    self.assertIn('address', response_data[0])
    self.assertIn('lat', response_data[0])
    self.assertIn('lon', response_data[0])
    self.assertIn('website', response_data[0])
    self.assertIn('zipcode', response_data[0])
    self.assertIn('phone', response_data[0])

    #testing datatypes of values
    self.assertIsInstance(response_data[0]['market_name'], str)
    self.assertIsInstance(response_data[0]['listing_id'], str)
    self.assertIsInstance(response_data[0]['address'], str)
    self.assertIsInstance(response_data[0]['lat'], str)
    self.assertIsInstance(response_data[0]['lon'], str)
    self.assertIsInstance(response_data[0]['website'], str)
    self.assertIsInstance(response_data[0]['zipcode'], str)
    self.assertIsInstance(response_data[0]['phone'], str)

  
#SAD PATH TESTING
  @responses.activate
  #something to note about this mock API key, utilizing it in the subsequent f-string, 
  #you can either use the mocked key itself, or the Environment variable which is USDA_API_KEY
  #The convention stated to use the env variable as it's closests to how the real code works
  @patch.dict('os.environ', {'USDA_API_KEY': 'your_mocked_api_key'})
  def test_get_market_locations_api_error(self):
      responses.add(responses.GET, f'{self.usda_api_url}?apikey={os.environ.get("USDA_API_KEY")}&zip={self.zipcode}&radius={self.radius}',
                    json={'error': 'API failure'}, status=500)

      response = self.client.get(self.endpoint)

      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
      self.assertJSONEqual(str(response.content, encoding='utf8'), {'error': 'There are no markets near you'})
