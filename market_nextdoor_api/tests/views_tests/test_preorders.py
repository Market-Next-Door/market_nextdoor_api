from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from market_nextdoor_api.models import Customer, Preorder, Item, Vendor
from market_nextdoor_api.serializers import PreorderSerializer

class PreorderViewTests(TestCase):
  def setUp(self):
    self.customer = Customer.objects.create(
      first_name="Michael",
      last_name="Myers",
      phone="1234567890",
      email="Mike@SmithsGroveSanutarium.org"
      )
    self.vendor = Vendor.objects.create(
      vendor_name="Elm Street Blades",
      first_name="Freddie",
      last_name="Krueger",
      phone="1234567890",
      email="Info@ElmStBlades.com",
      location="Springwood, OH"
      )
    self.item = Item.objects.create(
      item_name= "Axe",
      price= 10.99,
      size= "Average",
      availability= True,
      description= "A sharp axe prefered by the Jazz Man.",
      vendor= self.vendor
      )
    self.preorder_data = (
      'customer': self.customer.id,
      'item': self.item.id,
      'quantity_requested': 1,
      'ready': False
    )

  def test_get_preorder_list(self):
      url = f'/preorders/{self.customer.id}/'
      response = self.client.get(url)

      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(response.data), 1)
      self.assertEqual(response.data[0]["customer"], self.customer.id)

  def test_create_preorder(self):
      url = f'/preorders/{self.customer.id}/'
      response = self.client.post(url, data=self.preorder_data, format='json')

      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      # Add more assertions based on your expected response data

  def test_get_preorder_details(self):
      url = f'/preorders/{self.customer.id}/{self.preorder.id}/'
      response = self.client.get(url)

      self.assertEqual(response.status_code, status.HTTP_200_OK)
      # Add more assertions based on your expected response data

  def test_update_preorder(self):
      url = f'/preorders/{self.customer.id}/{self.preorder.id}/'
      updated_data = {'quantity_requested': 5}
      response = self.client.put(url, data=updated_data, format='json')

      self.assertEqual(response.status_code, status.HTTP_200_OK)
      # Add more assertions based on your expected response data

  def test_delete_preorder(self):
      url = f'/preorders/{self.customer.id}/{self.preorder.id}/'
      response = self.client.delete(url)

      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      self.assertFalse(Preorder.objects.filter(id=self.preorder.id).exists())
