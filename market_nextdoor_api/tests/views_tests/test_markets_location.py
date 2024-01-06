from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
import responses
import os
import pdb

class MarketLocationsTestCase(APITestCase):
  def setUp(self):
    pdb
    self.usda_api_url = "https://www.usdalocalfoodportal.com/api/farmersmarket/"
    self.zipcode = 84106
    self.radius = 10
    self.endpoint = reverse('get_market_locations', args=[self.zipcode, self.radius])
  @responses.activate
  #This utilizes the new library above to mock environment variables like the API key for USDA
  @patch.dict('os.environ', {'USDA_API_KEY': 'f@kekey123'})

   
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
    responses.add(responses.GET, f'{self.usda_api_url}?apikey={os.environ.get("USDA_API_KEY")}&zip={self.zipcode}&radius={self.radius}', json=mock_response, status=200)

    response = self.client.get(self.endpoint)
    response_data = response.json()
    #assertions about responses from the response keys
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIn('market_name', response_data[0])
    self.assertIn('address', response_data[0])
    self.assertIn('lat', response_data[0])
    self.assertIn('lon', response_data[0])
    self.assertIn('website', response_data[0])
    self.assertIn('zipcode', response_data[0])
    self.assertIn('phone', response_data[0])

    #testing datatypes of values
    self.assertIsInstance(response_data[0]['market_name'], str)
    self.assertIsInstance(response_data[0]['address'], str)
    self.assertIsInstance(response_data[0]['lat'], str)
    self.assertIsInstance(response_data[0]['lon'], str)
    self.assertIsInstance(response_data[0]['website'], str)
    self.assertIsInstance(response_data[0]['zipcode'], str)
    self.assertIsInstance(response_data[0]['phone'], str)

  
