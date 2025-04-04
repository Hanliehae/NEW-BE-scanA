from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    nim = models.CharField(max_length=15, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    telapak_tangan_kiri = models.ImageField(upload_to='hand_scans/', null=True, blank=True)
    telapak_tangan_kanan = models.ImageField(upload_to='hand_scans/', null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )

    class Meta:
        app_label = 'users'

    def __str__(self):
        return self.username
