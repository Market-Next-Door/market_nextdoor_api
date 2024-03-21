from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ...models import *
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
    self.preorder1 = Preorder2.objects.create(
      customer=self.customer,
      ready=False,
      packed=False,
      fulfilled=False,
    )
    self.preorderitem1 = Preorder2Item.objects.create(
      preorder=self.preorder1,
      item=self.item1,
      quantity_requested=2
    )
    self.preorderitem2 = Preorder2Item.objects.create(
      preorder=self.preorder1,
      item=self.item2,
      quantity_requested=1
    )

    self.preorder2 = Preorder2.objects.create(
      customer=self.customer,
      ready=False,
      packed=False,
      fulfilled=False,
    )
    Preorder2Item.objects.create(
      preorder=self.preorder2,
      item=self.item2,
      quantity_requested=2
    )
    Preorder2Item.objects.create(
      preorder=self.preorder2,
      item=self.item2,
      quantity_requested=1
    )

  def test_customer_preorder2_list(self):
    url =  reverse('preorder2_list', args=[self.customer.pk])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(len(response.data), 2)
    self.assertEqual(response.data[0]["customer"], self.customer.id)
    self.assertEqual(response.data[0]["ready"], self.preorder1.ready)
    self.assertEqual(response.data[0]["packed"], self.preorder1.packed)
    self.assertEqual(response.data[0]["fulfilled"], self.preorder1.fulfilled)
    self.assertEqual(len(response.data[0]["items"]), 2)
    self.assertEqual(response.data[0]["items"][0]["item_id"], self.item1.id)
    self.assertEqual(response.data[0]["items"][0]["vendor_id"], self.vendor1.id)
    self.assertEqual(response.data[0]["items"][0]["quantity_requested"], self.preorderitem1.quantity_requested)

  def test_customer_preorder2_no_customer(self):
    url =  reverse('preorder2_list', args=[20000])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND )

  def test_customer_preorder2_post(self):
    url = reverse('preorder2_list', args=[self.customer.pk])
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
    new_preorder = Preorder2.objects.last()
    first_preorder_item = Preorder2Item.objects.filter(preorder=new_preorder.pk, item_id=self.item1.pk)
    second_preorder_item = Preorder2Item.objects.filter(preorder=new_preorder.pk, item_id=self.item2.pk)

    self.assertEqual(response.data["id"], new_preorder.pk)
    self.assertEqual(response.data["customer"], new_preorder.customer.id)
    self.assertEqual(response.data["ready"], new_preorder.ready)
    self.assertEqual(response.data["packed"], new_preorder.packed)
    self.assertEqual(response.data["fulfilled"], new_preorder.fulfilled)
    self.assertEqual(len(response.data["items"]), 2)
    self.assertEqual(response.data["items"][0]["item_id"], new_preorder.items.first().id)
    self.assertEqual(response.data["items"][0]["item_name"], new_preorder.items.first().item_name)
    self.assertEqual(response.data["items"][0]["vendor_id"], new_preorder.items.first().vendor.id)
    self.assertEqual(response.data["items"][0]["quantity_requested"], first_preorder_item[0].quantity_requested)
    self.assertEqual(response.data["items"][1]["item_name"], new_preorder.items.last().item_name)
    self.assertEqual(response.data["items"][1]["vendor_id"], new_preorder.items.last().vendor.id)
    self.assertEqual(response.data["items"][1]["quantity_requested"], second_preorder_item[0].quantity_requested)

  def test_customer_preorder2_post_sad_path1(self): #customer # not passed in body
    url = reverse('preorder2_list', args=[self.customer.pk])
    data = {
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

    self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    self.assertEqual(response.data['customer'][0], 'This field is required.')

  def test_customer_preorder2_post_sad_path2(self): #Item does not exist
    url = reverse('preorder2_list', args=[self.customer.pk])
    wrong_id = 20000
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
                "item": wrong_id,
                "quantity": "2"
            }
        ]
    }
    json_data = json.dumps(data)

    response = self.client.post(url, data=json_data, content_type='application/json')

    self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    self.assertEqual(response.data['error'], f'Item {wrong_id} does not exist')

  def test_customer_preorder2_post_edge(self):
    #testing here to see if preorder can be created without adding items, because there is no data nested within 'items', it's not necessary to set data as JSON
    url = reverse('preorder2_list', args=[self.customer.pk])
    data = {
        "customer": self.customer.pk,
        "ready": "true",
        "packed": "false",
        "fulfilled": "false",
        "items": []
    }
    # json_data = json.dumps(data)
    response = self.client.post(url, data)

    self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    new_preorder = Preorder2.objects.last()
    self.assertEqual(len(response.data["items"]), 0)
    self.assertEqual(response.data["items"], [])

  def test_customer_preorder2_details(self):
    url =  reverse('preorder2_details', args=[self.customer.pk, self.preorder1.pk])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(response.data["id"], self.preorder1.id)
    self.assertEqual(response.data["customer"], self.preorder1.customer.id)
    self.assertEqual(response.data["ready"], self.preorder1.ready)
    self.assertEqual(response.data["packed"], self.preorder1.packed)
    self.assertEqual(response.data["fulfilled"], self.preorder1.fulfilled)
    self.assertEqual(len(response.data["items"]), 2)
    self.assertEqual(response.data["items"][0]["item_id"], self.preorderitem1.item_id)
    self.assertEqual(response.data["items"][0]["item_name"], self.item1.item_name)
    self.assertEqual(response.data["items"][0]["vendor_id"], self.item1.vendor.id)
    self.assertEqual(response.data["items"][0]["quantity_requested"], self.preorderitem1.quantity_requested)
    self.assertEqual(response.data["items"][1]["item_id"], self.preorderitem2.item_id)
    self.assertEqual(response.data["items"][1]["item_name"], self.item2.item_name)
    self.assertEqual(response.data["items"][1]["vendor_id"], self.item2.vendor.id)
    self.assertEqual(response.data["items"][1]["quantity_requested"], self.preorderitem2.quantity_requested)

  def test_customer_preorder2_details_sad1(self): #wrong customer passed
    url =  reverse('preorder2_details', args=[20000, self.preorder1.pk])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND )

  def test_customer_preorder2_details_sad2(self): #wrong preorder# passed
    url =  reverse('preorder2_details', args=[self.customer.pk, 2000000])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND )













