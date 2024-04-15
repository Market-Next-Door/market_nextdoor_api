from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from v2.models import *
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
      default_zipcode="80013"
    )
    self.vendor2 = Vendor.objects.create(
      vendor_name="Jimmy's Veggies",
      first_name="Little",
      last_name="Jimmy",
      phone="1234567890",
      email="timmy@gmail.com",
      password="1234567890",
      default_zipcode="80013"
    )

  def test_vendor_list(self):
    url =  reverse('full_vendor_list_v2')
    response = self.client.get(url)

    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(len(response.data), 2)
    self.assertEqual(response.data[0]["id"], self.vendor1.id)
    self.assertEqual(response.data[0]["vendor_name"], self.vendor1.vendor_name)
    self.assertEqual(response.data[0]["first_name"], self.vendor1.first_name)
    self.assertEqual(response.data[0]["last_name"], self.vendor1.last_name)
    self.assertEqual(response.data[0]["phone"], self.vendor1.phone)
    self.assertEqual(response.data[0]["email"], self.vendor1.email)
    self.assertEqual(response.data[0]["default_zipcode"], self.vendor1.default_zipcode)
    self.assertEqual(response.data[1]["id"], self.vendor2.id)
    self.assertEqual(response.data[1]["vendor_name"], self.vendor2.vendor_name)
    self.assertEqual(response.data[1]["first_name"], self.vendor2.first_name)
    self.assertEqual(response.data[1]["last_name"], self.vendor2.last_name)
    self.assertEqual(response.data[1]["phone"], self.vendor2.phone)
    self.assertEqual(response.data[1]["email"], self.vendor2.email)
    self.assertEqual(response.data[1]["default_zipcode"], self.vendor2.default_zipcode)

  def test_post_vendor(self):

    url =  reverse('full_vendor_list_v2')
    data = {
      "vendor_name": "John's Veggies",
      "first_name": "John",
      "last_name": "Harry",
      "phone": "1111111111",
      "email": "jh@gmail.com",
      "password": "123434",
      "default_zipcode": "80013"
    }
    response = self.client.post(url, data)
    self.assertEqual(response.status_code,status.HTTP_201_CREATED )
    self.assertEqual(Vendor.objects.count(), 3)
    self.assertEqual(response.data["id"], 3)
    self.assertEqual(response.data["vendor_name"], "John's Veggies")
    self.assertEqual(response.data["first_name"], "John")
    self.assertEqual(response.data["last_name"], "Harry")
    self.assertEqual(response.data["phone"], "1111111111")
    self.assertEqual(response.data["email"], "jh@gmail.com"),
    self.assertEqual(response.data["default_zipcode"], "80013")

  def test_vendor_details(self):
    url =  reverse('full_vendor_details_v2', args=[self.vendor1.pk])
    response = self.client.get(url)
    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(response.data["id"], self.vendor1.id)
    self.assertEqual(response.data["vendor_name"], self.vendor1.vendor_name)
    self.assertEqual(response.data["first_name"], self.vendor1.first_name)
    self.assertEqual(response.data["last_name"], self.vendor1.last_name)
    self.assertEqual(response.data["phone"], self.vendor1.phone)
    self.assertEqual(response.data["email"], self.vendor1.email)
    self.assertEqual(response.data["default_zipcode"], self.vendor1.default_zipcode)

  def test_update_vendor(self):
    url =  reverse('full_vendor_details_v2', args=[self.vendor1.pk])
    data = {
      "vendor_name": "John's Veggies",
      "first_name": "John",
      "last_name": "Harry",
      "phone": "1111111111",
      "email": "jh@gmail.com",
      "password": "123434",
      "default_zipcode": "80013"
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(Vendor.objects.count(), 2)
    self.assertEqual(response.data["id"], 1)
    self.assertEqual(response.data["vendor_name"], "John's Veggies")
    self.assertEqual(response.data["first_name"], "John")
    self.assertEqual(response.data["last_name"], "Harry")
    self.assertEqual(response.data["phone"], "1111111111")
    self.assertEqual(response.data["email"], "jh@gmail.com"),
    self.assertEqual(response.data["default_zipcode"], "80013")

  def test_delete_vendor(self):
    vendor_id = 1
    url =  reverse('full_vendor_details_v2', args=[vendor_id])

    response = self.client.delete(url)
    self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT )
    self.assertEqual(Vendor.objects.count(), 1)
