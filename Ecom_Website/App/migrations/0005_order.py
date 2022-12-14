# Generated by Django 4.0.6 on 2022-07-24 14:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0004_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ecommerce/order/image')),
                ('product', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=10)),
                ('date', models.DateField(default=datetime.datetime(2022, 7, 24, 19, 54, 39, 396061))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
