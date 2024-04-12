from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from v2.models import *
import pdb

class CustomerMarketTestCase(APITestCase):
    def setUp(self):
        self.market1 = Market.objects.create(
            market_name="Saturday Market",
            location="Denver, Co"
        )
        self.market2 = Market.objects.create(
            market_name="Sunday Market",
            location="Dallas, Tx"
        )
        self.customer1 = Customer.objects.create(
            first_name="George",
            last_name="Harrison",
            phone="1111111111",
            email="1@gmail.com",
            password="1234",
            default_zipcode="80013"
        )
        self.customer2 = Customer.objects.create(
            first_name="Dos",
            last_name="Secundus",
            phone="222222222",
            email="2@gmail.com",
            password="1234",
            default_zipcode="80013"
        )
        self.customer_market1 = CustomerMarket.objects.create(customer=self.customer1, market=self.market1)
        self.customer_market2 = CustomerMarket.objects.create(customer=self.customer1, market=self.market2)
        self.customer_market2 = CustomerMarket.objects.create(customer=self.customer2, market=self.market1)

    def test_get_customer_market_list(self):
        url = reverse('customer_market_list', args=[self.customer1.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["customer"], self.customer1.id)
        self.assertEqual(response.data[0]["market"], self.market1.id)
        self.assertEqual(response.data[1]["customer"], self.customer1.id)
        self.assertEqual(response.data[1]["market"], self.market2.id)

    def test_create_customer_market(self):
        data = {
            "customer": 2,
            "market": 2
        }
        url = reverse('customer_market_list', args=[self.customer2.pk])
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["customer"], self.customer2.id)
        self.assertEqual(response.data["market"], self.market2.id)

    def test_get_specific_customer_market(self):
        url = reverse('customer_market_details', args=[self.customer1.pk, self.market1.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["customer"], self.customer1.id)
        self.assertEqual(response.data["market"], self.market1.id)

    def test_delete_customer_market(self):
        url = reverse('customer_market_details', args=[self.customer1.pk, self.market1.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)