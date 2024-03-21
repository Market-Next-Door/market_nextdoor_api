from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ...models import *
import json

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

  def test_vendor_preorder2_list(self):#test  that only preorders with vendors associated appear
    url =  reverse('preorder2_vendor_list', args=[self.vendor1.pk])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]["customer"], self.customer.id)
    self.assertEqual(response.data[0]["ready"], self.preorder1.ready)
    self.assertEqual(response.data[0]["packed"], self.preorder1.packed)
    self.assertEqual(response.data[0]["fulfilled"], self.preorder1.fulfilled)
    self.assertEqual(len(response.data[0]["items"]), 2)
    self.assertEqual(response.data[0]["items"][0]["item_id"], self.item1.id)
    self.assertEqual(response.data[0]["items"][0]["vendor_id"], self.vendor1.id)
    self.assertEqual(response.data[0]["items"][0]["quantity_requested"], self.preorderitem1.quantity_requested)


  def test_vendor_preorder2_list_sad1(self):#wrong vendor passed
    url =  reverse('preorder2_vendor_list', args=[2000])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND )

  def test_vendor_preorder2_post(self):
    url = reverse('preorder2_vendor_list', args=[self.vendor1.pk])
    data = {
        "customer": self.customer.pk,
        "ready": "false",
        "packed": "false",
        "fulfilled": "false",
        "items": [
            {
                "item": self.item1.pk,
                "quantity": "5"
            },
            {
                "item": self.item1.pk,
                "quantity": "2"
            }
        ]
    }
    json_data = json.dumps(data)

    response = self.client.post(url, data=json_data, content_type='application/json')
    new_preorder = Preorder2.objects.last()
    preorder_items = Preorder2Item.objects.filter(preorder=new_preorder.pk, item_id=self.item1.pk)
    self.assertEqual(response.status_code,status.HTTP_201_CREATED)


    self.assertEqual(response.data["id"], new_preorder.pk)
    self.assertEqual(response.data["customer"], new_preorder.customer.id)
    self.assertEqual(response.data["ready"], new_preorder.ready)
    self.assertEqual(response.data["packed"], new_preorder.packed)
    self.assertEqual(response.data["fulfilled"], new_preorder.fulfilled)
    self.assertEqual(len(response.data["items"]), 2)
    self.assertEqual(response.data["items"][0]["item_id"], new_preorder.items.first().id)
    self.assertEqual(response.data["items"][0]["item_name"], new_preorder.items.first().item_name)
    self.assertEqual(response.data["items"][0]["vendor_id"], new_preorder.items.first().vendor.id)
    self.assertEqual(response.data["items"][0]["quantity_requested"], preorder_items[0].quantity_requested)
    self.assertEqual(response.data["items"][1]["item_name"], new_preorder.items.last().item_name)
    self.assertEqual(response.data["items"][1]["vendor_id"], new_preorder.items.last().vendor.id)
    self.assertEqual(response.data["items"][1]["quantity_requested"], preorder_items[1].quantity_requested)

  def test_vendor_preorder2_post_sad1(self): #body of request missing information
    url = reverse('preorder2_vendor_list', args=[self.vendor1.pk])
    data = {
        "ready": "false",
        "packed": "false",
        "fulfilled": "false",
        "items": [
            {
                "item": self.item1.pk,
                "quantity": "5"
            },
            {
                "item": self.item1.pk,
                "quantity": "2"
            }
        ]
    }
    json_data = json.dumps(data)

    response = self.client.post(url, data=json_data, content_type='application/json')
    self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    self.assertEqual(response.data['customer'][0], 'This field is required.')

  def test_vendor_preorder2_post_sad2(self): #Item does not exist
    url = reverse('preorder2_vendor_list', args=[self.vendor1.pk])
    wrong_id = 2000000
    data = {
        "customer": self.customer.pk,
        "ready": "false",
        "packed": "false",
        "fulfilled": "false",
        "items": [
            {
                "item": wrong_id,
                "quantity": "5"
            },
            {
                "item": self.item1.pk,
                "quantity": "2"
            }
        ]
    }
    json_data = json.dumps(data)

    response = self.client.post(url, data=json_data, content_type='application/json')
    self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    self.assertEqual(response.data['error'], f'Item {wrong_id} does not exist')

  def test_vendor_preorder2_post_sad3(self): #Vendor cannot creat orders if it's not their item
    url = reverse('preorder2_vendor_list', args=[self.vendor1.pk])
    data = {
        "customer": self.customer.pk,
        "ready": "false",
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
    self.assertEqual(response.data['error'], f'Item with ID {self.item2.pk} does not belong to vendor {self.vendor1.id}')

  def test_vendor_preorder2_details(self):
    url =  reverse('preorder2_vendor_details', args=[self.vendor1.pk, self.preorder1.pk])
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

  def test_vendor_preorder2_details_sad1(self): #wrong vendor passed
    url =  reverse('preorder2_vendor_details', args=[20000, self.preorder1.pk])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND )

  def test_vendor_preorder2_details_sad2(self): #No Preorder
    url =  reverse('preorder2_vendor_details', args=[self.vendor1.id, 20000])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND )
  
  def test_vendor_preorder2_details_sad3(self): #No item associated with vendor in preorder
    url =  reverse('preorder2_vendor_details', args=[self.vendor1.id, self.preorder2.pk])
    response = self.client.get(url) 

    self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST )
    self.assertEqual(response.data['error'], f'Preorder {self.preorder2.pk} does not have associated items with vendor {self.vendor1.id}')

  def test_vendor_preorder2_update(self):
    self.assertEqual(self.preorder1.ready, False)
    self.assertEqual(self.preorder1.packed, False)
    self.assertEqual(self.preorder1.fulfilled, False)

    url = reverse('preorder2_vendor_details', args=[self.vendor1.pk, self.preorder1.pk])
    data = {
        "ready": "true",
        "packed": "true",
        "fulfilled": "true",

    }

    response = self.client.put(url, data=data)
    self.assertEqual(response.status_code,status.HTTP_200_OK)
    updated_preorder = Preorder2.objects.get(id=self.preorder1.pk)
    self.assertEqual(response.data["ready"], updated_preorder.ready)
    self.assertEqual(response.data["packed"], updated_preorder.packed)
    self.assertEqual(response.data["fulfilled"], updated_preorder.fulfilled)


  def test_vendor_preorder2_delete(self):
    url = reverse('preorder2_vendor_details', args=[self.vendor1.pk, self.preorder1.pk])

    self.assertEqual(Preorder2.objects.count(), 2)
    response = self.client.delete(url)
    self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT )
    self.assertEqual(Preorder2.objects.count(), 1)
    self.assertEqual(response.data, None)