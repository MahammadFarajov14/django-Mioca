# Generated by Django 5.1.5 on 2025-04-27 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
