from django.db import models

# Create your models here.


class Customer(models.Model): #One customer can make many orders
     # stored as a string with a maximum length of 100 characters.
    name = models.CharField(max_length=100)
    #  must be unique in the database to avoid duplicates
    email = models.EmailField(unique=True)
    # Returns a string representation of the customer
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.customer}"


from django.db import models
from django.contrib.auth.models import Customer

# Create your models here.
# Represents an order placed by a customer.
class Order(models.Model):
     # ForeignKey relationship to the Customer model.
    # This indicates that each order is associated with one customer.

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Date when the order was placed, automatically set to the current date when the order is created.
    order_date = models.DateField(auto_now_add=True)
     # Total amount of the order, stored as a decimal number with up to 10 digits and 2 decimal places.
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Returns a string representation of the order, including the order ID and associated customer's name.
    def __str__(self):
        return f"Order #{self.id} - {self.customer}"