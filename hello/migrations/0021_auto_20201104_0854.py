# Generated by Django 3.0.8 on 2020-11-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0020_auto_20201103_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(blank=True, max_length=20, verbose_name=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field = models.CharField(max_length=50, blank=True, verbose_name="name"),
            
        ),
    ]