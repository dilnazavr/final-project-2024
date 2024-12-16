import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('postgresql://postgres:22112005@localhost/exam_platform')
    SECRET_KEY = os.getenv('SECRET_KEY', '22112005')