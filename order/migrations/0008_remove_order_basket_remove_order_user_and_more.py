# Generated by Django 5.1.7 on 2025-04-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_wishlist_is_active_wishlist_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='basket',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='useraddress',
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='', max_length=200, verbose_name='country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='lname',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
