# Generated by Django 2.2.7 on 2019-11-19 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countrydata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='continent',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='country',
            name='country',
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='countrydata.Continent'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='area',
            field=models.PositiveIntegerField(verbose_name='area'),
        ),
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(max_length=50, verbose_name='capital'),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(default='', max_length=5, unique=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.PositiveIntegerField(verbose_name='population'),
        ),
    ]
