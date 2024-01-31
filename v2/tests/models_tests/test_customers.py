from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ...models import *
import pdb

class CustomerModelTest(TestCase):
  def setUp(self):
    self.customer = Customer.objects.create(
      first_name="George",
      last_name="Harrison",
      phone="1111111111",
      email="gh@gmail.com"
    )

  def test_model_fields(self):
      customer = Customer.objects.get(first_name=self.customer.first_name)
      # Test the values of the fields
      self.assertEqual(customer.first_name, self.customer.first_name)
      self.assertEqual(customer.last_name, self.customer.last_name)
      self.assertEqual(customer.phone, self.customer.phone)
      self.assertEqual(customer.email, self.customer.email)
