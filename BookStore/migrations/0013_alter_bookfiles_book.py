# Generated by Django 4.2.3 on 2023-07-23 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0012_alter_book_options_alter_orderedbook_order_bookfiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookfiles',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file', to='BookStore.book'),
        ),
    ]
