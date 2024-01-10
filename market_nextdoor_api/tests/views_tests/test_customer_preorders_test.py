from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ...models import *
import requests
import json
import pdb

class CustomerPreorderTestCase(APITestCase):
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

  def test_customer_preorder_test_post(self):
    url = reverse('preorder_test_list', args=[self.customer.pk])
    data = {
        "customer": self.customer.pk,
        "ready": "true",
        "packed": "false",
        "fulfilled": "false",
        "items": [
            {
                "item": self.item1.pk,
                "quantity": "5"
            },
            {
                "item": self.item2.pk,
                "quantity": "2"
            }
        ]
    }
    json_data = json.dumps(data)

    response = self.client.post(url, data=json_data, content_type='application/json')

    self.assertEqual(response.status_code,status.HTTP_201_CREATED )
    new_preorder = Preorder_test.objects.last()
    first_preorder_item = Preorder_testItem.objects.filter(preorder=new_preorder.pk, item_id=self.item1.pk)
    second_preorder_item = Preorder_testItem.objects.filter(preorder=new_preorder.pk, item_id=self.item2.pk)
    # pdb.set_trace()
    self.assertEqual(response.data["id"], new_preorder.pk)
    self.assertEqual(response.data["customer"], new_preorder.customer.id)
    self.assertEqual(response.data["ready"], new_preorder.ready)
    self.assertEqual(response.data["packed"], new_preorder.packed)
    self.assertEqual(response.data["fulfilled"], new_preorder.fulfilled)
    self.assertEqual(len(response.data["items"]), 2)
    self.assertEqual(response.data["items"][0]["item_id"], new_preorder.items.first().id)
    self.assertEqual(response.data["items"][0]["item_name"], new_preorder.items.first().item_name)
    self.assertEqual(response.data["items"][0]["vendor_id"], new_preorder.items.first().vendor.id)
    self.assertEqual(response.data["items"][0]["quantity"], first_preorder_item[0].quantity)
    self.assertEqual(response.data["items"][1]["item_name"], new_preorder.items.last().item_name)
    self.assertEqual(response.data["items"][1]["vendor_id"], new_preorder.items.last().vendor.id)
    self.assertEqual(response.data["items"][1]["quantity"], second_preorder_item[0].quantity)








