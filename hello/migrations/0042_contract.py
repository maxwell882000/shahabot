# Generated by Django 3.1.3 on 2021-02-27 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0041_happybirthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='contract/main')),
            ],
        ),
    ]