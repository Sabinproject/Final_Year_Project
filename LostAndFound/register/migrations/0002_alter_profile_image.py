# Generated by Django 3.2.6 on 2021-08-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/default.jpeg', upload_to='register/images'),
        ),
    ]