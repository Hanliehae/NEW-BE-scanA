from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .mahasiswa import Mahasiswa
from .mata_kuliah import MataKuliah
from .jadwal import Jadwal
from .kehadiran import Kehadiran
