# Generated by Django 2.1.2 on 2018-11-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nama',
            field=models.CharField(default='', max_length=120),
        ),
    ]
