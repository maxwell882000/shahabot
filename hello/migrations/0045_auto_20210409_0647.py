# Generated by Django 3.1.3 on 2021-04-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0044_auto_20210401_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='status',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='status',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
