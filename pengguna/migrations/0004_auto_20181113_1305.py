# Generated by Django 2.1.2 on 2018-11-13 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0003_auto_20181113_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='kelas',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='st_jurulatih',
            field=models.CharField(default='', max_length=120),
        ),
    ]