from django.db import models
from courses.models import MataKuliah

class Jadwal(models.Model):
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    semester = models.IntegerField()
    tahun_akademik = models.CharField(max_length=10)
    pertemuan_ke = models.IntegerField()
    hari = models.CharField(max_length=20)
    tanggal = models.DateField()
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()

    def __str__(self):
        return f"{self.mata_kuliah.nama_mk} - Pertemuan {self.pertemuan_ke}"
