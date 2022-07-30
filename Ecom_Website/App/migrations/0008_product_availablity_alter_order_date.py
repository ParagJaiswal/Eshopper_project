# Generated by Django 4.0.6 on 2022-07-25 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_brand_alter_sub_category_options_alter_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availablity',
            field=models.CharField(choices=[('In Stock', 'In Stock'), ('Out Of Stock', 'Out Of Stock')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 7, 25, 18, 34, 39, 430385)),
        ),
    ]
