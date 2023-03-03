# Generated by Django 3.2.13 on 2023-03-03 09:31

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dokumen', '0006_auto_20230301_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokumen',
            name='kategori',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dokumen.category'),
        ),
    ]
