# Generated by Django 3.1.3 on 2020-11-25 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0034_auto_20201122_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof_pre_value',
            name='inn',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ИНН'),
        ),
        migrations.AddField(
            model_name='profile',
            name='inn',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ИНН'),
        ),
    ]
