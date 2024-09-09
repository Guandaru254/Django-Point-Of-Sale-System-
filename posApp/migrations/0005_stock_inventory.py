# Generated by Django 5.0.3 on 2024-07-22 16:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0004_salesitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('units_of_measure', models.CharField(max_length=50)),
                ('quantity_available', models.PositiveIntegerField()),
                ('recorded_value', models.PositiveBigIntegerField()),
                ('factory_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('wholesale_pice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retail_prices', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supplier_prices', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_supplier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('Quantity_Available', models.IntegerField(default=0)),
                ('Quantity_Stored', models.IntegerField(default=0)),
                ('Factory_price', models.FloatField(default=0)),
                ('Wholesale_price', models.FloatField(default=0)),
                ('Retail_pice', models.FloatField(default=0)),
                ('product_location', models.CharField(max_length=150)),
                ('Kg_price', models.FloatField(default=0)),
                ('Supplier_price', models.FloatField(default=0)),
                ('Purchases_Account', models.CharField(max_length=150)),
                ('Sales_Account', models.CharField(max_length=150)),
                ('status', models.IntegerField(default=1)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posApp.category')),
            ],
        ),
    ]
