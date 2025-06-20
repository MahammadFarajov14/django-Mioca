# Generated by Django 5.1.7 on 2025-04-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_order_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=200, verbose_name='city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=200, verbose_name='phone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=200, verbose_name='state'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='zip',
            field=models.CharField(default='', max_length=200, verbose_name='zip'),
            preserve_default=False,
        ),
    ]
