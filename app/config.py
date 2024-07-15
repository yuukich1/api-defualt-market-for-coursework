from dotenv import load_dotenv
import os


load_dotenv()

DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')
DB_URL = os.getenv('DB_URL')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
REDIS_URL = os.getenv('REDIS_URL')

IMAGE_DIRECTOR_URL = './image'

SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')


db_full_url = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
