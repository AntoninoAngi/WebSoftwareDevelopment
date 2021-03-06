# Generated by Django 2.2.7 on 2020-01-28 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200115_1539'),
        ('games', '0005_auto_20200128_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sold_games', to='games.Game')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchased_games', to='accounts.Profile')),
            ],
        ),
    ]
