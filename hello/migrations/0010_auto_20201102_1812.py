# Generated by Django 3.0.8 on 2020-11-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_auto_20201102_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='login',
            field=models.CharField(max_length=50, null=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='parol',
            field=models.CharField(max_length=50, null=True, verbose_name='Парол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pseudonym',
            field=models.CharField(max_length=50, null=True, verbose_name='Псевдоним'),
        ),
    ]
