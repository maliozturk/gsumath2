# Generated by Django 2.1.7 on 2019-03-15 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gonderiler', '0003_user_okul_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='okul_no',
            field=models.IntegerField(unique=True),
        ),
    ]
