from django.db import models

class Market(models.Model):
    market_name = models.CharField(max_length=50)
    location = models.CharField(max_length =100)
    details = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.market_name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length = 10, null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Vendor(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=True)
    vendor_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name

class Item(models.Model):
    item_name = models.CharField(max_length=50)
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
        return self.item_name

class Preorder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    quantity_requested = models.IntegerField(default=1)
    ready = models.BooleanField(default=False)
    packed = models.BooleanField(default=False)
    fulfilled = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

#ManytoMany Test Models
class Preorder2(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    items = models.ManyToManyField(Item, through='Preorder2Item')
    ready = models.BooleanField(default=False)
    packed = models.BooleanField(default=False)
    fulfilled = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Preorder2Item(models.Model):
    preorder = models.ForeignKey(Preorder2, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    quantity_requested = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity_requested} of {self.item.item_name} in {self.preorder}"

class Customer2(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length = 10, null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Vendor2(models.Model):
    vendor_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name
    
class Market2(models.Model):
    market_name = models.CharField(max_length=50)
    location = models.CharField(max_length =100)
    details = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    vendors = models.ManyToManyField(Vendor2, through='Vendor2Market')
    vendors = models.ManyToManyField(Customer2, through='Customer2Market')
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.market_name
    
class Customer2Market(models.Model):
    customer = models.ForeignKey(Customer2, on_delete=models.CASCADE, null=False)
    market = models.ForeignKey(Market2, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name} at {self.market.market_name}"

class Vendor2Market(models.Model):
    vendor = models.ForeignKey(Vendor2, on_delete=models.CASCADE, null=False)
    market = models.ForeignKey(Market2, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.vendor.vendor_name} at {self.market.market_name}"