from django.db import models

class MataKuliah(models.Model):
    id_mk = models.CharField(max_length=10, unique=True)
    nama_mk = models.CharField(max_length=100)
    semester = models.IntegerField()
    tahun_akademik = models.CharField(max_length=10)

    class Meta:
        app_label = 'courses'

    def __str__(self):
        return self.nama_mk
