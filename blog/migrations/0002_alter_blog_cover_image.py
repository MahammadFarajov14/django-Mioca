# Generated by Django 5.1.5 on 2025-02-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_image',
            field=models.ImageField(blank=True, default='blog_images/1.jpg', null=True, upload_to='blog_images/'),
        ),
    ]
