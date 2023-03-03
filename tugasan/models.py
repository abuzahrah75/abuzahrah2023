from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Tugasan(MPTTModel):
    STATUS_TUGAS =(
        ('0', 'Tidak Aktif'),
        ('1', 'Aktif'),
        ('2', 'Dalam Proses'),
        ('3', 'Selesai'),
        ('4', 'Batal'),)

    nama = models.CharField(max_length=250, default='')
    st_tugas = models.CharField(max_length=2, choices=STATUS_TUGAS, default=0)
    kumpulan = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['kumpulan']


    def __str__(self):
        return f'{self.nama}'
