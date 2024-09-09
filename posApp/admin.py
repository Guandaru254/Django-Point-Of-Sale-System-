from typing import Any
from django.contrib import admin,messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from posApp.models import Category, Creditor, Debtors, Products, Sales, Store, inventory, salesItems,Stock

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)
admin.site.register(inventory)
admin.site.register(Debtors)
admin.site.register(Creditor)
admin.site.register(Stock)
admin.site.register(Store)
# admin.site.register(Employees)