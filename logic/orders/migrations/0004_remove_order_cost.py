# Generated by Django 2.2.10 on 2020-03-25 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cost',
        ),
    ]