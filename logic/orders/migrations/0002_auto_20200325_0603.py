# Generated by Django 2.2.10 on 2020-03-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='schedule_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('U', 'unclaimed'), ('S', 'scheduled'), ('F', 'finished'), ('C', 'canceled')], default='U', max_length=1),
        ),
    ]
