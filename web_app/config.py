import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    MONGODB_URI = os.environ.get("MONGODB_URI")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = 'web_app/static/images'