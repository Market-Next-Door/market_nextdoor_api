from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ...models import *
import pdb

class VendorTestCase(APITestCase):
  def setUp(self):
    self.vendor1 = Vendor.objects.create(
      vendor_name="Timmy's Veggies",
      first_name="Little",
      last_name="Timmy",
      phone="1234567890",
      email="timmy@gmail.com",
      password="1234567890",
      location="1234 Main St, Anytown, USA",
    )

  def test_vendor_list(self):
    url =  reverse('vendor_list')
    response = self.client.get(url)

    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]["id"], self.vendor1.id)
    self.assertEqual(response.data[0]["vendor_name"], self.vendor1.vendor_name)
    self.assertEqual(response.data[0]["first_name"], self.vendor1.first_name)
    self.assertEqual(response.data[0]["last_name"], self.vendor1.last_name)
    self.assertEqual(response.data[0]["phone"], self.vendor1.phone)
    self.assertEqual(response.data[0]["email"], self.vendor1.email)
    self.assertEqual(response.data[0]["location"], self.vendor1.location)

  def test_post_vendor(self):

    url =  reverse('vendor_list')
    data = {
      "vendor_name": "John's Veggies",
      "first_name": "John",
      "last_name": "Harry",
      "phone": "1111111111",
      "email": "jh@gmail.com",
      "password": "123434",
      "location": "1234 Main St, Anytown, USA"
    }
    response = self.client.post(url, data)
    self.assertEqual(response.status_code,status.HTTP_201_CREATED )
    self.assertEqual(Vendor.objects.count(), 2)
    self.assertEqual(response.data["id"], 2)
    self.assertEqual(response.data["vendor_name"], "John's Veggies")
    self.assertEqual(response.data["first_name"], "John")
    self.assertEqual(response.data["last_name"], "Harry")
    self.assertEqual(response.data["phone"], "1111111111")
    self.assertEqual(response.data["email"], "jh@gmail.com"),
    self.assertEqual(response.data["location"], "1234 Main St, Anytown, USA")

  def test_vendor_details(self):
    url =  reverse('vendor_details', args=[self.vendor1.pk])
    response = self.client.get(url)
    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(response.data["id"], self.vendor1.id)
    self.assertEqual(response.data["vendor_name"], self.vendor1.vendor_name)
    self.assertEqual(response.data["first_name"], self.vendor1.first_name)
    self.assertEqual(response.data["last_name"], self.vendor1.last_name)
    self.assertEqual(response.data["phone"], self.vendor1.phone)
    self.assertEqual(response.data["email"], self.vendor1.email)
    self.assertEqual(response.data["location"], self.vendor1.location)

  def test_update_vendor(self):
    url =  reverse('vendor_details', args=[self.vendor1.pk])
    data = {
      "vendor_name": "John's Veggies",
      "first_name": "John",
      "last_name": "Harry",
      "phone": "1111111111",
      "email": "jh@gmail.com",
      "password": "123434",
      "location": "1234 Main St, Anytown, USA"
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(Vendor.objects.count(), 1)
    self.assertEqual(response.data["id"], 1)
    self.assertEqual(response.data["vendor_name"], "John's Veggies")
    self.assertEqual(response.data["first_name"], "John")
    self.assertEqual(response.data["last_name"], "Harry")
    self.assertEqual(response.data["phone"], "1111111111")
    self.assertEqual(response.data["email"], "jh@gmail.com"),
    self.assertEqual(response.data["location"], "1234 Main St, Anytown, USA")

  def test_delete_vendor(self):
    vendor_id = 1
    url =  reverse('vendor_details', args=[vendor_id])

    response = self.client.delete(url)
    self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT )
    self.assertEqual(Vendor.objects.count(), 0)
    
                     