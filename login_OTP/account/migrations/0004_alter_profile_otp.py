# Generated by Django 4.2.1 on 2023-09-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='otp',
            field=models.IntegerField(default=False),
        ),
    ]
