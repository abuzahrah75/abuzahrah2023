# Generated by Django 3.2.13 on 2023-02-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0005_auto_20181116_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]