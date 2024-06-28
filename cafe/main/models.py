from django.db import models

# Create your models here.
class Coffee(models.Model):
    coffeeName = models.CharField(max_length=100)
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    totalCount = models.IntegerField()
    coffeeImage = models.ImageField(upload_to='coffeeImages/')

    def __str__(self):
        return self.coffeeName
    
    class Meta:
        db_table = 'coffee'

class Customers(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=8)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='orders')
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.coffee.coffeeName} for {self.customer.name} on {self.order_date}"

    class Meta:
        db_table = 'orders'