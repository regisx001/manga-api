# Generated by Django 4.0.8 on 2023-07-14 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar/%Y/%m/%d/'),
        ),
    ]