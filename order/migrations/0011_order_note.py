# Generated by Django 5.1.7 on 2025-04-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_order_address_order_city_order_phone_order_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
