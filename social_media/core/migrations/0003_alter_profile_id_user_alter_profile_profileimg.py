# Generated by Django 4.1.5 on 2023-05-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank.webp', upload_to='profile_file'),
        ),
    ]
