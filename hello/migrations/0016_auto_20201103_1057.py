# Generated by Django 3.0.8 on 2020-11-03 05:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0015_auto_20201103_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Номер телефона необходимо вводить в формате «+999999999». Допускается до 15 цифр.', regex='^\\+?1?\\d{9,15}$')], verbose_name=''),
        ),
    ]