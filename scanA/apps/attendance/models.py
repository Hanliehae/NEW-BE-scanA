from django.db import models
from users.models import User
from schedule.models import Jadwal
from courses.models import MataKuliah

class Enrollment(models.Model):
    mahasiswa = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('mahasiswa', 'mata_kuliah')

    def __str__(self):
        return f"{self.mahasiswa.username} - {self.mata_kuliah.nama_mk}"

class Presensi(models.Model):
    mahasiswa = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE)
    status_kehadiran = models.CharField(max_length=10, choices=[('Hadir', 'Hadir'), ('Tidak Hadir', 'Tidak Hadir')])
    waktu_scan = models.DateTimeField(auto_now_add=True)
    foto_scan = models.ImageField(upload_to='scan_attendance/', null=True, blank=True)

    def __str__(self):
        return f"{self.mahasiswa.username} - {self.jadwal.mata_kuliah.nama_mk} - {self.status_kehadiran}"
