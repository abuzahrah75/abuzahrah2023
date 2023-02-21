# Generated by Django 3.2.13 on 2023-02-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mycrud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default='=', max_length=250)),
                ('nama_app', models.CharField(default='', max_length=100)),
                ('nama_model', models.CharField(default='', max_length=100)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Tidak Aktif'), (1, 'Aktif'), (2, 'Batal')], default=0)),
                ('header_display', models.CharField(default='mycrud/temp//header_display.html', max_length=200)),
                ('data_fields', models.CharField(default='mycrud/temp/data_fields.html', max_length=200)),
                ('to_view', models.CharField(default='mycrud/temp/detail_view.html', max_length=200)),
                ('edit_form', models.CharField(default='=', max_length=100)),
                ('edit_part', models.BooleanField(default=False)),
                ('edit_partial', models.CharField(default='-', max_length=200)),
                ('to_actions', models.BooleanField(default=False)),
                ('to_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
