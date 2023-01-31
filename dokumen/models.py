from django.db import models




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
