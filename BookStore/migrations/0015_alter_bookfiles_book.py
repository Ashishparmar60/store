# Generated by Django 4.2.3 on 2023-07-23 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0014_alter_bookfiles_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookfiles',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='BookStore.book'),
        ),
    ]
