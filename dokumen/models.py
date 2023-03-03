from django.db import models
from mptt.models import MPTTModel, TreeForeignKey



# class for list of documents model
# setiap dokumen akan di beri tajuk dan kategori + details yg lain
class Dokumen(models.Model):
    STATUS_DOCS = (
        ('0', 'Tidak Aktif'),
        ('1', 'Aktif'),
        ('2', 'Dalam Proses'),
        ('3', 'Selesai'),
        ('4', 'Batal'),)

    nama = models.CharField(max_length=250, default='Documents Template')
    keterangan = models.CharField(max_length=250, default='-')
    status_dokumen = models.CharField(max_length=2, choices=STATUS_DOCS, default=0)
    kategori = TreeForeignKey('Category', null=True,blank=True, on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'{self.nama}'

class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __str__(self):
        return f'{self.name}'


class SectJenis(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class Docs_template(models.Model):
    nama = models.CharField(max_length=250, default='Documents Template')
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nama}'

class TempSection(models.Model):
    nama = models.CharField(max_length=250, default='section')
    jenis = models.ForeignKey(SectJenis, on_delete=models.CASCADE)
    tempName = models.ForeignKey(Docs_template, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nama}'
