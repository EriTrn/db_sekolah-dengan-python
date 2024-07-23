from django.db import models

# Create your models here.

from django.db import models

class Siswa(models.Model):
    nis = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    tanggal_lahir = models.DateField()

    def __str__(self):
        return self.nama