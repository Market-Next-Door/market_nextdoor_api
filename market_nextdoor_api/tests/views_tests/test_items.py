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

# POST request test
def test_post_item(self):
  url = reverse('item_list', args=[self.vendor1.pk])
  data = {
    'item_name': "Tomato", 
    'vendor': 1, 
    'price': 1.99, 
    'size': "1lbs", 
    'quantity': 45, 
    'availability': True, 
    'description': "Nice and fresh tomatoes!"
  }
  response = self.client.post(url, data)
  self.assertEqual(response.status_code,status.HTTP_201_CREATED)
  self.assertEqual(Item.objects.count(), 3)
  self.assertEqual(response.data["id"], Item.objects.last().id)
  self.assertEqual(response.data["item_name"], "Tomato")
  self.assertEqual(response.data["vendor"], self.vendor1.id)
  self.assertEqual(response.data["price"], '1.99')
  self.assertEqual(response.data["size"], "1lbs")
  self.assertEqual(response.data["quantity"], 45),
  self.assertEqual(response.data["availability"], True)
  self.assertEqual(response.data["description"], "Nice and fresh tomatoes!")

# GET (show) request test
def test_item_details(self):
  url =  reverse('item_details', args=[self.vendor1.pk, self.item1.pk])
  response = self.client.get(url)
  self.assertEqual(response.status_code,status.HTTP_200_OK )
  self.assertEqual(response.data["id"], self.item1.id)
  self.assertEqual(response.data["vendor"], self.vendor1.id)
  self.assertEqual(response.data["price"], self.item1.price)
  self.assertEqual(response.data["size"], self.item1.size)
  self.assertEqual(response.data["quantity"], self.item1.quantity)
  self.assertEqual(response.data["availability"], self.item1.availability)
  self.assertEqual(response.data["description"], self.item1.description)

# PUT request test
def test_update_item(self):
  url =  reverse('item_details', args=[self.vendor1.pk, self.item1.pk])
  data = {
    'item_name': "Tomato", 
    'vendor': 1, 
    'price': 99.99, 
    'size': "10lbs", 
    'quantity': 5, 
    'availability': True, 
    'description': "Nice, fresh, and HUGE tomatoes! Cures all illnesses! Maybe not, but are you gonna take that risk??"
  }
  response = self.client.put(url, data, format='json')
  self.assertEqual(response.status_code,status.HTTP_200_OK )
  self.assertEqual(Vendor.objects.count(), 1)
  self.assertEqual(response.data["id"], self.item1.id)
  self.assertEqual(response.data["vendor"], self.vendor1.id)
  self.assertEqual(response.data["price"], "99.99")
  self.assertEqual(response.data["size"], "10lbs")
  self.assertEqual(response.data["quantity"], 5)
  self.assertEqual(response.data["availability"], self.item1.availability)
  self.assertEqual(response.data["description"], "Nice, fresh, and HUGE tomatoes! Cures all illnesses! Maybe not, but are you gonna take that risk??")

# DELETE request test
def test_delete_item(self):
  self.assertEqual(Item.objects.count(), 2)
  url =  reverse('item_details', args=[self.vendor1.pk, self.item1.pk])
  response = self.client.delete(url)
  self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT )
  self.assertEqual(Item.objects.count(), 1)
