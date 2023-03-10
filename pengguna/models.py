from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	nama = models.CharField(max_length=120,default='')
	nokp = models.CharField(max_length=15,default='')
	jantina = models.CharField(max_length=15, default='', blank=True)
	telefon = models.CharField(max_length=21, default='', blank=True)
	noahli = models.CharField(max_length=15, default='', blank=True)
	st_ahli = models.CharField(max_length=15, default='', blank=True)
	st_belajar = models.CharField(max_length=15, default='', blank=True)
	st_bwg = models.CharField(max_length=7, default='Putih')
	kelas = models.CharField(max_length=120, default='', blank=True)
	st_jurulatih = models.CharField(max_length=120, default='', blank=True)


	def __str__(self):
	   	return f'{self.user.profile.nama} Profile'

	def save(self, *args, **kwargs):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
