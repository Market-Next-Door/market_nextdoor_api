from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from v1.models import Customer, Item, Vendor, Preorder
from v1.serializers import PreorderSerializer
from django.urls import reverse
import pdb

class PreorderViewTests(TestCase):
  def setUp(self):
    self.customer = Customer.objects.create(
        first_name="John",
        last_name="Doe",
        phone="1234567890",
        email="john.doe@example.com"
    )
    self.vendor = Vendor.objects.create(
        vendor_name="Sample Vendor",
        first_name="Vendor",
        last_name="Person",
        phone="9876543210",
        email="vendor@example.com",
        location="Sample Location"
    )
    self.item = Item.objects.create(
        item_name="Sample Item",
        price=19.99,
        size="Medium",
        availability=True,
        description="A sample item description.",
        vendor=self.vendor
    )
    self.valid_preorder_data = {
        'customer': self.customer.id,
        'item': self.item.id,
        'quantity_requested': 2,
        'ready': False
    }
    self.invalid_preorder_data = {
        'item': self.item.id,
        'quantity_requested': 2
    }

  def test_preorder_list_get_happy_path(self):
    url = f'/api/v1/customers/{self.customer.id}/preorders/'
    # url = reverse('preorder_list', [self.customer.pk])
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 0)
    self.assertEqual(response.data, [])

  def test_preorder_list_post_happy_path(self):
    url = f'/api/v1/customers/{self.customer.id}/preorders/'
    # url = reverse('preorder_list', [self.customer.pk])
    response = self.client.post(url, data=self.valid_preorder_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Preorder.objects.count(), 1)

  def test_preorder_list_post_sad_path(self):
    url = f'/api/v1/customers/{self.customer.id}/preorders/'
    # url = reverse('preorder_list', [self.customer.pk])
    response = self.client.post(url, data=self.invalid_preorder_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(Preorder.objects.count(), 0)

  def test_preorder_details_get_happy_path(self):
    preorder = Preorder.objects.create(
        customer=self.customer,
        item=self.item,
        quantity_requested=2,
        ready=False
    )
    url = f'/api/v1/customers/{self.customer.id}/preorders/{preorder.id}/'
    # url = reverse('preorder_list', [self.customer.pk, self.valid_preorder_data.pk])
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['customer'], self.customer.id)
    self.assertEqual(response.data['item'], self.item.id)
    self.assertEqual(response.data['quantity_requested'], 2)

  def test_preorder_details_get_sad_path(self):
    url = f'/api/v1/customers/{self.customer.id}/preorders/9999999/'
    # url = reverse('preorder_list', [self.customer.pk, self.invalid_preorder_data.pk])
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_preorder_details_put_happy_path(self):
    preorder = Preorder.objects.create(
        customer=self.customer,
        item=Item.objects.create(item_name="Sample Item", price=19.99, size="Medium", availability=True, description="A sample item description.", vendor=self.vendor),
        quantity_requested=2,
        ready=False
    )
    url = f'/api/v1/customers/{self.customer.id}/preorders/{preorder.id}/'
    # url = reverse('preorder_list', [self.customer.pk, self.valid_preorder_data.pk])
    data = self.valid_preorder_data

    response = self.client.put(url, data=data, content_type='application/json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    updated_preorder = Preorder.objects.get(pk=preorder.id)
    self.assertEqual(updated_preorder.quantity_requested, data['quantity_requested'])

  def test_preorder_details_put_sad_path(self):
    url = f'/api/v1/preorders/{self.customer.id}/9999999/'
    # url = reverse('preorder_list', [self.customer.pk, self.valid_preorder_data.pk])
    data = self.valid_preorder_data

    response = self.client.put(url, data=data, format='json')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_preorder_details_delete_happy_path(self):
    preorder = Preorder.objects.create(
      customer=self.customer,
      item=Item.objects.create(item_name="Sample Item", price=19.99, size="Medium", availability=True, description="A sample item description.", vendor=self.vendor),
      quantity_requested=2,
      ready=False
    )
    url = f'/api/v1/customers/{self.customer.id}/preorders/{preorder.id}/'
    # url = reverse('preorder_list', [self.customer.pk, self.valid_preorder_data.pk])

    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertFalse(Preorder.objects.filter(id=preorder.id).exists())
    self.assertEqual(Preorder.objects.count(), 0)

  def test_preorder_details_delete_sad_path(self):
    url = f'/api/v1/customers/{self.customer.id}/preorders/9999999/'
    # url = reverse('preorder_list', [self.customer.pk, self.invalid_preorder_data.pk])
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    self.assertEqual(Preorder.objects.count(), 0)
