# Generated by Django 3.2.6 on 2021-08-27 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]