# Generated by Django 4.2.3 on 2023-07-21 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0009_alter_customer_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
    ]
