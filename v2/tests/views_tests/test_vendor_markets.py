from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from v2.models import *
import pdb

class VendorMarketTestCase(APITestCase):
    def setUp(self):
        self.market1 = Market.objects.create(
            market_name="Saturday Market",
            location="Denver, Co"
        )
        self.market2 = Market.objects.create(
            market_name="Sunday Market",
            location="Dallas, Tx"
        )
        self.vendor1 = Vendor.objects.create(
            vendor_name="All Day Potatoes",
            first_name="George",
            last_name="Harrison",
            phone="1111111111",
            email="1@gmail.com",
            password="1234",
            default_zipcode="80013"
        )
        self.vendor2 = Vendor.objects.create(
            vendor_name="secondvendor",
            first_name="Dos",
            last_name="Secundus",
            phone="222222222",
            email="2@gmail.com",
            password="1234",
            default_zipcode="80013"
        )
        self.vendor_market1 = VendorMarket.objects.create(vendor=self.vendor1, market=self.market1)
        self.vendor_market2 = VendorMarket.objects.create(vendor=self.vendor1, market=self.market2)
        self.vendor_market2 = VendorMarket.objects.create(vendor=self.vendor2, market=self.market1)

    def test_get_vendor_market_list(self):
        url = reverse('vendor_market_list', args=[self.vendor1.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["vendor"], self.vendor1.id)
        self.assertEqual(response.data[0]["market"], self.market1.id)
        self.assertEqual(response.data[0]["active"], True)
        self.assertEqual(response.data[1]["vendor"], self.vendor1.id)
        self.assertEqual(response.data[1]["market"], self.market2.id)
        self.assertEqual(response.data[1]["active"], True)

    def test_create_vendor_market(self):
        data = {
            "vendor": 2,
            "market": 2
        }
        url = reverse('vendor_market_list', args=[self.vendor2.pk])
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["vendor"], self.vendor2.id)
        self.assertEqual(response.data["market"], self.market2.id)

    def test_get_specific_vendor_market(self):
        url = reverse('vendor_market_details', args=[self.vendor1.pk, self.market1.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["vendor"], self.vendor1.id)
        self.assertEqual(response.data["market"], self.market1.id)
        self.assertEqual(response.data["active"], True)

    def test_update_vendor_market(self):
        updated_data = { "active": False }
        url = reverse('vendor_market_details', args=[self.vendor1.pk, self.market1.pk])
        response = self.client.put(url, updated_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["active"], updated_data["active"])

    def test_delete_vendor_market(self):
        url = reverse('vendor_market_details', args=[self.vendor1.pk, self.market1.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)