# Generated by Django 2.2.8 on 2020-08-13 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Esta es una description de prueba para la categoria de smartphones.'),
            preserve_default=False,
        ),
    ]