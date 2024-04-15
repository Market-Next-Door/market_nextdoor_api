from django.test import TestCase
from v2.models import Customer, Market, CustomerMarket
from v2.serializers import CustomerMarketSerializer

class CustomerMarketSerializerTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            phone="1234567890",
            email="test@example.com",
            password="securepassword",
            default_zipcode="80013"
        )
        self.market = Market.objects.create(
            market_name="Test Market",
            location="Test Location",
            details="Test Details"
        )
        self.customer_market = CustomerMarket.objects.create(
            customer=self.customer,
            market=self.market
        )

    def test_customer_market_serializer(self):
        serializer = CustomerMarketSerializer(instance=self.customer_market)
        self.assertEqual(serializer.data['customer'], self.customer.id)
        self.assertEqual(serializer.data['market'], self.market.id)
        self.assertIsNotNone(serializer.data['date_created'])
        self.assertIsNotNone(serializer.data['updated_at'])
