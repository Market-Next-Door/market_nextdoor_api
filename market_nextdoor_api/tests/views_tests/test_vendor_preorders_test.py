from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ...models import *
import pdb

class VendorPreorderTestCase(APITestCase):
  def setUp(self):
    self.market = Market.objects.create(
      market_name="Saturday Market",
      location="Denver, TX"
    )
    self.vendor1 = Vendor.objects.create(
      market=self.market,
      vendor_name="All Day Potatoes",
      first_name="George",
      last_name="Harrison",
      phone="1111111111",
      email="1@gmail.com",
      password="1234",
      location="Denver, CO"
    )
    self.vendor2 = Vendor.objects.create(
      market=self.market,
      vendor_name="secondvendor",
      first_name="2",
      last_name="2",
      phone="1111111111",
      email="1@gmail.com",
      password="1234",
      location="Denver, CO"
    )
    self.item1 = Item.objects.create(
      item_name="potato",
      vendor=self.vendor1,
      price="23.20",
      quantity="10",
      availability=True,
      description="11231"
    )
    self.item2 = Item.objects.create(
      item_name="seconditem",
      vendor=self.vendor2,
      price="23.20",
      quantity="10",
      availability=True,
      description="11231"
    )
    self.customer = Customer.objects.create(
      first_name="Jo",
      last_name="Jack",
      phone="1222222222",
      email="1@gmail.com",
      password="1234",
      location="Denver, CO"
    )
    self.preorder1 = Preorder_test.objects.create(
      customer=self.customer,
      ready=False,
      packed=False,
      fulfilled=False,
    )
    self.preorderitem1 = Preorder_testItem.objects.create(
      preorder=self.preorder1,
      item=self.item1,
      quantity=2
    )
    Preorder_testItem.objects.create(
      preorder=self.preorder1,
      item=self.item2,
      quantity=1
    )

    self.preorder2 = Preorder_test.objects.create(
      customer=self.customer,
      ready=False,
      packed=False,
      fulfilled=False,
    )
    Preorder_testItem.objects.create(
      preorder=self.preorder2,
      item=self.item2,
      quantity=2
    )
    Preorder_testItem.objects.create(
      preorder=self.preorder2,
      item=self.item2,
      quantity=1
    )

  def test_vendor_preorder_test_list(self):
    url =  reverse('preorder_test_vendor_list', args=[self.vendor1.pk])
    response = self.client.get(url) #test  that only preorders with vendors associated appear
    # pdb.set_trace()

    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]["customer"], self.customer.id)
    self.assertEqual(response.data[0]["ready"], self.preorder1.ready)
    self.assertEqual(response.data[0]["packed"], self.preorder1.packed)
    self.assertEqual(response.data[0]["fulfilled"], self.preorder1.fulfilled)
    self.assertEqual(len(response.data[0]["items"]), 2)
    self.assertEqual(response.data[0]["items"][0]["item_id"], self.item1.id)
    self.assertEqual(response.data[0]["items"][0]["vendor_id"], self.vendor1.id)
    self.assertEqual(response.data[0]["items"][0]["quantity"], self.preorderitem1.quantity)






