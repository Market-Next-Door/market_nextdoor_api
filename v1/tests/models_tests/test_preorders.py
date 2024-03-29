from django.test import TestCase
from v1.models import Preorder, Customer, Item, Vendor

class PreorderModelTest(TestCase):
  def setUp(self):
    self.customer = Customer.objects.create(
      first_name="Michael",
      last_name="Myers",
      phone="1234567890",
      email="Mike@SmithsGroveSanutarium.org"
      )
    self.customer2 = Customer.objects.create(
      first_name="Jason",
      last_name="Voorhees",
      phone="1234567890",
      email="Jason@CampCrystalLake.com"
      )
    self.vendor = Vendor.objects.create(
      vendor_name="Elm Street Blades",
      first_name="Freddie",
      last_name="Krueger",
      phone="1234567890",
      email="Info@ElmStBlades.com",
      location="Springwood, OH"
      )
    self.vendor2 = Vendor.objects.create(
      vendor_name="Overlook Distillery",
      first_name="Jack",
      last_name="Torrence",
      phone="1234567890",
      email="JDE@MileHighDrinks.com",
      location="Stovington, NH"
      )
    self.item = Item.objects.create(
      item_name= "Axe",
      price= 10.99,
      size= "Average",
      availability= True,
      description= "A sharp axe prefered by the Jazz Man.",
      vendor= self.vendor
      )
    self.item2 = Item.objects.create(
      item_name= "Hunting Knife",
      price= 65.99,
      size= "Large",
      availability= True,
      description= "Large Knife used for hunting Sidney.",
      vendor= self.vendor
      )
    self.item3 = Item.objects.create(
      item_name= "Romulan Ale",
      price= 5399.99,
      size= "Small Bottle",
      availability= True,
      description= "A highly intoxicating beverage, which is outlawed within the Federation",
      vendor = self.vendor2
      )
    self.item4 = Item.objects.create(
      item_name= "Redrum",
      price= 10.00,
      size= "Large",
      availability= True,
      description= "A large bottle of Redrum.",
      vendor = self.vendor2
      )
  def test_preorder_creation(self):
    preorder = Preorder.objects.create(
        customer=self.customer,
        item=self.item,
        quantity_requested=1,
        ready=False
    )

    self.assertEqual(preorder.customer, self.customer)
    self.assertEqual(preorder.item, self.item)
    self.assertEqual(preorder.quantity_requested, 1)
    self.assertFalse(preorder.ready)
    self.assertIsNotNone(preorder.date_created)
    self.assertIsNotNone(preorder.updated_at)

  def test_default_values(self):
    preorder = Preorder.objects.create(customer=self.customer, item=self.item)

    self.assertEqual(preorder.quantity_requested, 1)
    self.assertFalse(preorder.ready)
    self.assertIsNotNone(preorder.date_created)
    self.assertIsNotNone(preorder.updated_at)
    
