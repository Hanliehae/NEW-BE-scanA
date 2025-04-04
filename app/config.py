import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', "postgresql://postgres:ppl123@localhost:5432/BEscanA")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
