# Generated by Django 4.2.3 on 2023-07-21 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0006_remove_book_genre_book_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedbook',
            name='quantity',
        ),
    ]
