# Generated by Django 3.0.8 on 2020-11-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0019_auto_20201103_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='day_payment',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Дата оплата'),
        ),
    ]
