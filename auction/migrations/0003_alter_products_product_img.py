# Generated by Django 4.1.3 on 2023-01-21 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_products_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_img',
            field=models.ImageField(blank=True, upload_to='auction/images/'),
        ),
    ]
