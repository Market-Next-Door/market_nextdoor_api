from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ...models import *
import pdb

class CustomerTestCase(APITestCase):
  def setUp(self):
    self.customer1 = Customer.objects.create(
      first_name="George",
      last_name="Harrison",
      phone="1234567890",
      email="george@gmail.com",
    )
    self.customer2 = Customer.objects.create(
      first_name="Janey",
      last_name="Harrison",
      phone="1234567890",
      email="janey@gmail.com",
    )

  def test_customer_list(self):
    url =  reverse('customer_list')
    response = self.client.get(url)

    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(len(response.data), 2)
    self.assertEqual(response.data[0]["id"], self.customer1.id)
    self.assertEqual(response.data[0]["first_name"], self.customer1.first_name)
    self.assertEqual(response.data[0]["last_name"], self.customer1.last_name)
    self.assertEqual(response.data[0]["phone"], self.customer1.phone)
    self.assertEqual(response.data[0]["email"], self.customer1.email)
    self.assertEqual(response.data[1]["id"], self.customer2.id)
    self.assertEqual(response.data[1]["first_name"], self.customer2.first_name)
    self.assertEqual(response.data[1]["last_name"], self.customer2.last_name)

  def test_post_customer(self):

    url =  reverse('customer_list')
    data = {
      "first_name": "John",
      "last_name": "Harry",
      "phone": "1111111111",
      "email": "jh@gmail.com",
      "password": "123434"
    }
    response = self.client.post(url, data)
    self.assertEqual(response.status_code,status.HTTP_201_CREATED )
    self.assertEqual(Customer.objects.count(), 3)
    self.assertEqual(response.data["id"], 3)
    self.assertEqual(response.data["first_name"], "John")
    self.assertEqual(response.data["last_name"], "Harry")
    self.assertEqual(response.data["phone"], "1111111111")
    self.assertEqual(response.data["email"], "jh@gmail.com")
    self.assertEqual(response.data["location"], None)

  def test_customer_details(self):
    url =  reverse('customer_details', args=[self.customer1.pk])
    response = self.client.get(url)

    self.assertEqual(Customer.objects.count(), 2)
    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(response.data["id"], 1)
    self.assertEqual(response.data["first_name"], "George")
    self.assertEqual(response.data["last_name"], "Harrison")
    self.assertEqual(response.data["phone"], Customer.objects.get(id=1).phone)
    self.assertEqual(response.data["email"], Customer.objects.get(id=1).email)

  def test_update_customer_details(self):
    customer_id = 1
    url =  reverse('customer_details', args=[customer_id])
    data = {
      "first_name": "UPDATE",
      "last_name": "UPDATE",
      "phone": "UPDATE",
      "email": "UPDATE",
      "location": "UPDATE"
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(Customer.objects.count(), 2)
    self.assertEqual(response.data["id"], 1)
    self.assertEqual(response.data["first_name"], "UPDATE")
    self.assertEqual(response.data["last_name"], "UPDATE")
    self.assertEqual(response.data["phone"], "UPDATE")
    self.assertEqual(response.data["email"], "UPDATE")
    self.assertEqual(response.data["location"], "UPDATE")


  def test_delete_customer(self):
    customer_id = 1
    url =  reverse('customer_details', args=[customer_id])

    response = self.client.delete(url)
    self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT )
    self.assertEqual(Customer.objects.count(), 1)
    self.assertEqual(response.data, None)



