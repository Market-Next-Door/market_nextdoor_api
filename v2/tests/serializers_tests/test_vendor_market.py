from django.test import TestCase
from v2.models import CustomerMarket, Customer, Market
from v2.serializers import CustomerMarketSerializer

class CustomerMarketSerializerTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            phone="1234567890",
            email="test@example.com",
            password="securepassword",
            default_zipcode="80013",
        )
        self.market = Market.objects.create(
            market_name="Test Market",
            location="Test Location",
            details="Test Details",
            start_date="2023-01-01",
            end_date="2023-01-02",
        )
        self.customer_market = CustomerMarket.objects.create(
            customer=self.customer,
            market=self.market,
        )

        self.serializer_data = {
            'id': self.customer_market.id,
            'customer': self.customer.id,
            'market': self.market.id,
        }

    def test_customer_market_serializer(self):
        serializer = CustomerMarketSerializer(instance=self.customer_market)
        self.assertEqual(serializer.data['customer'], self.customer.id)
        self.assertEqual(serializer.data['market'], self.market.id)

    def test_customer_market_deserializer(self):
        serializer = CustomerMarketSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        deserialized_data = serializer.validated_data
        self.assertEqual(deserialized_data['customer'], self.customer)
        self.assertEqual(deserialized_data['market'], self.market)
