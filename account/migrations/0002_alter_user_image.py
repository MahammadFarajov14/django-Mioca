# Generated by Django 5.1.5 on 2025-02-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='images/default-profile.jpg', null=True, upload_to='user', verbose_name='image'),
        ),
    ]
