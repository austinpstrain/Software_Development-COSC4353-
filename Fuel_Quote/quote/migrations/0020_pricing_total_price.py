# Generated by Django 3.0.7 on 2020-07-12 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0019_remove_pricing_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='total_price',
            field=models.FloatField(null=True),
        ),
    ]
