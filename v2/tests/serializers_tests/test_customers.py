from rest_framework.test import APITestCase
from django.test import TestCase
from v2.serializers import *
import pdb

class CustomerSerializerTest(TestCase):
  def test_customer_serializer(self):
    data = {
      "id": "1",
      "first_name": "George",
      "last_name": "Harrison",
      "phone": "1111111111",
      "email": "gh@gmail.com",
      "password": "1234",
      "default_zipcode": "80013"
    }
    serializer = CustomerSerializer(data=data)

    self.assertTrue(serializer.is_valid())

class CustomerSerializerInvalidTest(TestCase):
  def test_customer_invalid_serializer(self):
    data = {
      "id": "1",
      "first_name": "George",
      "last_name": "Harrison",
      "phone": "1111111111",
      "email": "gh@gmail.com",
      "default_zipcode": "80013" 
    }
    serializer = CustomerSerializer(data=data)
    self.assertFalse(serializer.is_valid())

    self.assertNotEqual(serializer.errors, {})


