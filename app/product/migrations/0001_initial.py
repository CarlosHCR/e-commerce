# Generated by Django 4.2.3 on 2023-07-28 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30, verbose_name='Color')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(error_messages={'unique': 'This size already exists.'}, max_length=5, unique=True, verbose_name='Size')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'This product already exists in storage.'}, max_length=30, unique=True, verbose_name='Name')),
                ('price', models.FloatField(verbose_name='price')),
                ('description_short', models.TextField(verbose_name='Description short')),
                ('description_long', models.TextField(verbose_name='Description long')),
                ('image', models.ImageField(upload_to='products', verbose_name='image')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('discount_price', models.FloatField(blank=True, null=True, verbose_name='Discount price')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.color', verbose_name='Color')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.size', verbose_name='Size')),
            ],
        ),
    ]
