# Generated by Django 3.1.3 on 2020-12-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0039_auto_20201203_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='acc_pre_value',
            name='notification',
            field=models.CharField(max_length=20, null=True, verbose_name='Уведомления'),
        ),
        migrations.AddField(
            model_name='account',
            name='notification',
            field=models.CharField(blank=True, max_length=20, verbose_name='Уведомления'),
        ),
    ]
