# Generated by Django 4.2.6 on 2023-10-14 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('product_info', models.CharField(blank=True, max_length=100000, null=True)),
                ('product_image', models.ImageField(upload_to='uploads')),
                ('image1', models.ImageField(blank=True, upload_to='uploads')),
                ('image2', models.ImageField(blank=True, upload_to='uploads')),
                ('image3', models.ImageField(blank=True, upload_to='uploads')),
                ('image4', models.ImageField(blank=True, upload_to='uploads')),
                ('image5', models.ImageField(blank=True, upload_to='uploads')),
                ('image6', models.ImageField(blank=True, upload_to='uploads')),
                ('quanitity', models.PositiveBigIntegerField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('product_vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.vendor')),
            ],
        ),
    ]