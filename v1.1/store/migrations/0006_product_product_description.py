# Generated by Django 4.2.6 on 2023-10-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]