from django.db import models



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

    def __str__(self):
        return f'{self.nama}'

class Category(models.Model):
    nama = models.CharField(max_length=250, default='Documents Template')

    def __str__(self):
        return f'{self.nama}'


class SectJenis(models.Model):
    nama = models.CharField(max_length=250, default='Documents Template')

    def __str__(self):
        return f'{self.nama}'


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
