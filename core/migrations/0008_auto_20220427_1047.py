# Generated by Django 3.2.8 on 2022-04-27 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201206_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='item',
            name='labels',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]
