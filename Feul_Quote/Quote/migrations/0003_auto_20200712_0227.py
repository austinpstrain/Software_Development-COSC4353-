# Generated by Django 3.0.7 on 2020-07-12 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quote', '0002_auto_20200712_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getquote',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quote.Customer'),
        ),
    ]