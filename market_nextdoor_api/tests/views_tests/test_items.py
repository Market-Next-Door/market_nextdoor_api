from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ...models import *
import pdb

class ItemTestCase(APITestCase):
  def setUp(self):
    self.market = Market.objects.create(
      market_name="Saturday Market",
      location="Denver, TX"
    )
    self.vendor1 = Vendor.objects.create(
      vendor_name="Tom's Toms!",
      first_name="Thomas",
      last_name="Tomatillo",
      phone="123-456-7890",
      email="lets-ketchup@gmail.com",
      password="password",
      location="123 Zesty St, Tomatotown, USA",
    )
    self.item1 = Item.objects.create(
      item_name="potato",
      vendor=self.vendor1,
      price="23.20",
      quantity=10,
      availability=True,
      description="11231"
    )
    self.item2 = Item.objects.create(
      item_name="seconditem",
      vendor=self.vendor1,
      price="23.20",
      quantity=10,
      availability=True,
      description="11231"
    )

# GET (index) request Test
  def test_item_list(self):
    url = reverse('item_list', args=[self.vendor1.pk])
    response = self.client.get(url)
    self.assertEqual(response.status_code,status.HTTP_200_OK)
    self.assertEqual(response.data[0]["id"], self.item1.id)
    self.assertEqual(response.data[0]["item_name"], self.item1.item_name)
    self.assertEqual(response.data[0]["vendor"], self.vendor1.id)
    self.assertEqual(response.data[0]["price"], self.item1.price)
    self.assertEqual(response.data[0]["size"], self.item1.size)
    self.assertEqual(response.data[0]["quantity"], self.item1.quantity)
    self.assertEqual(response.data[0]["availability"], self.item1.availability)
    self.assertEqual(response.data[0]["description"], self.item1.description)
    self.assertEqual(response.data[0]["image"], self.item1.image)

