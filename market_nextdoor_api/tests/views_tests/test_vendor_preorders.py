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
    self.preorder1 = Preorder.objects.create(
      customer=self.customer,
      item=self.item1,
      quantity_requested=1,
      ready=False
    )
    self.preorder2 = Preorder.objects.create(
      customer=self.customer,
      item=self.item1,
      quantity_requested=1,
      ready=False
    )
    self.preorder3 = Preorder.objects.create(
      customer=self.customer,
      item=self.item2,
      quantity_requested=1,
      ready=False
    )

  def test_vendor_preorder_list(self):
    url =  reverse('preorder_vendor_list', args=[self.vendor1.pk])
    response = self.client.get(url)

    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(len(response.data), 2)
    self.assertEqual(response.data[0]["vendor_id"], self.vendor1.id)
    self.assertEqual(response.data[1]["vendor_id"], self.vendor1.id)
    self.assertEqual(response.data[1]["customer"], self.customer.id)
    self.assertEqual(response.data[1]["item"], self.preorder2.item.id)
    self.assertEqual(response.data[1]["ready"], self.preorder2.ready)

    url =  reverse('preorder_vendor_list', args=[self.vendor2.pk])
    response = self.client.get(url)
    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]["vendor_id"], self.vendor2.id)


  def test_vendor_preorder_details(self):
    url =  reverse('preorder_vendor_list_details', args=[self.vendor1.pk, self.preorder1.pk])
    response = self.client.get(url)
    self.assertEqual(Customer.objects.count(), 1)
    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(response.data["id"], 1)
    self.assertEqual(response.data["ready"], self.preorder1.ready)
    self.assertEqual(response.data["vendor_id"], self.vendor1.id)


  def test_update_preorder_details(self):
    url =  reverse('preorder_vendor_list_details', args=[self.vendor1.pk, self.preorder1.pk])
    data = {
      "ready": True
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(Customer.objects.count(), 1)
    self.assertEqual(response.status_code,status.HTTP_200_OK )
    self.assertEqual(response.data["id"], 1)
    self.assertEqual(response.data["ready"], True)
    self.assertEqual(response.data["vendor_id"], self.vendor1.id)




