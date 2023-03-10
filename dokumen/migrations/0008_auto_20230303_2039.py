# Generated by Django 3.2.13 on 2023-03-03 12:39

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dokumen', '0007_dokumen_kategori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docs_template',
            name='kategori',
        ),
        migrations.AddField(
            model_name='docs_template',
            name='extra_info',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='docs_template',
            name='jenis_item',
            field=models.PositiveSmallIntegerField(choices=[(0, 'N.A.'), (1, 'Struktur'), (2, 'Data')], default=1),
        ),
        migrations.AddField(
            model_name='docs_template',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docs_template',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docs_template',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='dokumen.docs_template'),
        ),
        migrations.AddField(
            model_name='docs_template',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='docs_template',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sectjenis',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sectjenis',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sectjenis',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sectjenis',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
    ]
