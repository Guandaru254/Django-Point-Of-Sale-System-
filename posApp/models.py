from datetime import datetime
from unicodedata import category
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

# Create your models here.

# class Employees(models.Model):
#     code = models.CharField(max_length=100,blank=True) 
#     firstname = models.TextField() 
#     middlename = models.TextField(blank=True,null= True) 
#     lastname = models.TextField() 
#     gender = models.TextField(blank=True,null= True) 
#     dob = models.DateField(blank=True,null= True) 
#     contact = models.TextField() 
#     address = models.TextField() 
#     email = models.TextField() 
#     department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
#     position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
#     date_hired = models.DateField() 
#     salary = models.FloatField(default=0) 
#     status = models.IntegerField() 
#     date_added = models.DateTimeField(default=timezone.now) 
#     date_updated = models.DateTimeField(auto_now=True) 

    # def __str__(self):
    #     return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Products(models.Model):
    code = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField(default=0)
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code + " - " + self.name

class Sales(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code

class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)

class inventory(models.Model):
    name = models.TextField()
    description = models.TextField()
    Quantity_Available = models.IntegerField(default=0)

    def __str__(self):
        return self.code + " - " + self.name
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stock(models.Model):
    product_name = models.CharField(max_length=150, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    reorder_level = models.IntegerField(default=150)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        store_name = self.store.name if self.store else "No Store"
        return f"{self.product_name} - {store_name}"

    def stock_status(self):
        if self.quantity is None or self.reorder_level:
            return "Low"
        elif self.quantity <= self.reorder_level * 2:
            return "Medium"
        else:
            return "High"
    
    def needs_reorder(self):
        if self.quantity is None or self.reorder_level is None:
            return False
        return self.quantity <= self.reorder_level
    
    def clean(self):
        if self.quantity < 0:
            raise ValidationError('Quantity cannot be negative')
        if self.reorder_level is not None and self.reorder_level < 0:
            raise ValidationError('Reorder level cannot be negative')
        
    def save(self, *args, **kwargs):
        if self.pk is None:  # Only set the stock number if it's a new instance
            max_stock_number = Stock.objects.filter(store=self.store).aggregate(models.Max('stock_number'))['stock_number__max']
            self.stock_number = (max_stock_number or 0) + 1
        super(Stock, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('product_name', 'store')


class Debtors(models.Model):
    name = models.CharField(max_length=150)
    amount_owed = models.DecimalField(max_digits=10,decimal_places=2)
    date_owed = models.DateField()

    def __str__(self):
        return self.name
    
class Creditor(models.Model):
    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return self.name
    

class SalesReport(models.Model):
    report_name = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.report_name