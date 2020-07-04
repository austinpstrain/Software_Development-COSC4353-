# Generated by Django 3.0.7 on 2020-07-04 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_auto_20200703_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='name',
        ),
        migrations.AddField(
            model_name='quote',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quote.Customer'),
        ),
        migrations.AddField(
            model_name='quote',
            name='delivery_address1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='delivery_address2',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
