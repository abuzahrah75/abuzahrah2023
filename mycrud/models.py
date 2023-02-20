from django.db import models


class Mycrud(models.Model):
    STATUS_TUGAS = (
        (0, 'Tidak Aktif'),
        (1, 'Aktif'),
        (2, 'Batal'),)

    nama = models.CharField(max_length=250, default='=')
    nama_app = models.CharField(max_length=100, default='')
    nama_model = models.CharField(max_length=100, default='')
    status = models.PositiveSmallIntegerField(choices=STATUS_TUGAS, default=0)

    header_display = models.CharField(max_length=200, default='mycrud/temp//header_display.html')
    data_fields = models.CharField(max_length=200, default='mycrud/temp/data_fields.html')
    to_view = models.CharField(max_length=200, default='mycrud/temp/detail_view.html')
    edit_form = models.CharField(max_length=100, default='=')
    edit_part = models.BooleanField(default=False)
    edit_partial = models.CharField(max_length=200, default='-')
    to_actions=models.BooleanField(default=False)
    to_delete = models.BooleanField(default=False)
    

    # header_display = models.CharField(max_length=250, default='=')

  

    def __str__(self):
        return f'{self.pk} : {self.nama_app} - {self.nama_model}'

