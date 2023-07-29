# Generated by Django 4.2.3 on 2023-07-29 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=20, verbose_name='Ref Code')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Start Date')),
                ('ordered_date', models.DateTimeField(verbose_name='Ordered Date')),
                ('received', models.BooleanField(default=False, verbose_name='Received')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orderitem', verbose_name='Order Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
