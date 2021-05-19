# Generated by Django 3.0.8 on 2020-11-09 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0023_auto_20201104_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='summa',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='card_number',
            field=models.CharField(max_length=30, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_card',
            field=models.DateField(default='2020-10-10', verbose_name='Срок карты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='owner_card',
            field=models.CharField(max_length=100, null=True, verbose_name='Владелец карты'),
        ),
        migrations.AddField(
            model_name='profile',
            name='prefix',
            field=models.CharField(max_length=20, null=True, verbose_name='ID партнера'),
        ),
        migrations.AddField(
            model_name='profile',
            name='type_payment',
            field=models.CharField(max_length=50, null=True, verbose_name='Способ оплаты'),
        ),
        migrations.AddField(
            model_name='profile',
            name='valute_card',
            field=models.CharField(max_length=10, null=True, verbose_name='Валюта карты'),
        ),
    ]