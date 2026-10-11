import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from uygulama.veritabani import veritabani_baslat
from uygulama.ayarlar import Ayarlar

load_dotenv()

# Ayar seçici (geliştirme / üretim)
ayar_secici = {
    "gelistirme": Ayarlar,
    "production": Ayarlar  # İstersen ayrı Production sınıfı tanımlayabilirsin
}

def uygulama_olustur(ayar_adi="gelistirme"):
    # Flask uygulamasını sablonlar klasörü ile başlat
    uygulama = Flask(__name__, template_folder="sablonlar")

    # 1) Ayarları yükle
    secilen_ayar = ayar_secici.get(ayar_adi, ayar_secici["gelistirme"])
    uygulama.config.from_object(secilen_ayar)

    # 2) CORS ayarı
    CORS(uygulama)

    # 3) Veritabanı başlat
    with uygulama.app_context():
        veritabani_baslat(uygulama)

    # 4) Rotaları tanıt
    from uygulama.rotalar import api_arayuzu, sayfa_arayuzu
    uygulama.register_blueprint(api_arayuzu, url_prefix="/api")
    uygulama.register_blueprint(sayfa_arayuzu)

    return uygulama
