# Generated by Django 2.2.7 on 2020-01-25 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200115_1539'),
        ('games', '0002_auto_20200123_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='accounts.Profile'),
        ),
    ]
