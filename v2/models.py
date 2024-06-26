from django.db import models

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    default_zipcode = models.CharField(max_length=255, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name

class Item(models.Model):
    item_name = models.CharField(max_length=50, null=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=25, null=True)
    quantity = models.IntegerField(default=1, null=False)
    availability = models.BooleanField(default=False)
    description = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True) 

    def delete(self):
        self.image.delete()
        super().delete()

    def __str__(self):
        return f"{self.item_name} from {self.vendor.vendor_name}"

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length = 10, null=True)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    default_zipcode = models.CharField(max_length=55, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Preorder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    quantity_requested = models.IntegerField(default=1, null=False)
    ready = models.BooleanField(default=False)
    packed = models.BooleanField(default=False)
    fulfilled = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity_requested} of {self.item.item_name} for {self.customer.first_name}"

class Market(models.Model):
    market_name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length =100, null=True)
    listing_id = models.CharField(max_length=50, null=False)
    details = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    vendors = models.ManyToManyField(Vendor, through='VendorMarket')
    customers = models.ManyToManyField(Customer, through='CustomerMarket')
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.market_name
    
class CustomerMarket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name} at {self.market.market_name}"
    
class VendorMarket(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=False)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vendor.vendor_name} at {self.market.market_name}"