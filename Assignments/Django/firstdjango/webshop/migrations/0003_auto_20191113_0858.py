# Generated by Django 2.2.7 on 2019-11-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_auto_20191113_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.BigIntegerField(default=0),
        ),
    ]
