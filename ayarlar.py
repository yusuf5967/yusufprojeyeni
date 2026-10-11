import os
from dotenv import load_dotenv
load_dotenv() # .env dosyasındaki gizli ayarları oku

class Ayarlar:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'susams59')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'akilli_satis.db')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', ' ')
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    BUSINESS_CONTEXT = os.environ.get('BUSINESS_CONTEXT', 'Learn&Live eğitim platformu')
    CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', 'https://yusufakn035.wixstudio.com/my-site-1')