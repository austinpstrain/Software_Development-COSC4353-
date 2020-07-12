# Generated by Django 3.0.7 on 2020-07-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0012_pricing_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='user',
        ),
        migrations.AddField(
            model_name='pricing',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]