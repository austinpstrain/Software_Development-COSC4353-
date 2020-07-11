# Generated by Django 3.0.7 on 2020-07-11 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quote', '0016_auto_20200705_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='quote',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
