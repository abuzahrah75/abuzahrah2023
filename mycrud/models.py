from django.db import models


class Mycrud(models.Model):
    STATUS_TUGAS = (
        ('0', 'Tidak Aktif'),
        ('1', 'Aktif'),
        ('2', 'Dalam Proses'),
        ('3', 'Selesai'),
        ('4', 'Batal'),)

    nama = models.CharField(max_length=250, default='=')
    nama_app = models.CharField(max_length=250, default='')
    nama_model = models.CharField(max_length=250, default='')
    st_tugas = models.CharField(max_length=2, choices=STATUS_TUGAS, default=0)

    def __str__(self):
        return f'{self.nama}'

