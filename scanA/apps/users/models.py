
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """#+
    This class represents a user in the system. It extends the AbstractUser class provided by Django.#+
#+
    Attributes:#+
    ROLE_CHOICES: A list of tuples representing the available roles for a user.#+
#+
    role: A CharField representing the user's role. It can be either 'admin' or 'student'.#+
#+
    nim: A CharField representing the user's NIM (only applicable for students). It is unique and can be null or blank.#+
#+
    phone: A CharField representing the user's phone number. It can be null or blank.#+
#+
    profile_pic: An ImageField representing the user's profile picture. It is stored in the 'profile_pics/' directory and can be null or blank.#+
#+
    telapak_tangan_kiri: An ImageField representing the user's left hand scan. It is stored in the 'hand_scans/' directory and can be null or blank.#+
#+
    telapak_tangan_kanan: An ImageField representing the user's right hand scan. It is stored in the 'hand_scans/' directory and can be null or blank.#+
#+
    Methods:#+
    __str__: Returns the username of the user.#+
    """#+
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    nim = models.CharField(max_length=15, unique=True, null=True, blank=True)  # Hanya mahasiswa punya NIM
    phone = models.CharField(max_length=15, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    telapak_tangan_kiri = models.ImageField(upload_to='hand_scans/', null=True, blank=True)
    telapak_tangan_kanan = models.ImageField(upload_to='hand_scans/', null=True, blank=True)

    def __str__(self):
        return self.username
