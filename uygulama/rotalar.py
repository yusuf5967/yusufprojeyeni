from flask import Blueprint, render_template, request, jsonify
from uygulama.veritabani import musteri_adayi_ekle, tum_adaylari_getir
from uygulama.servisler import yapay_zeka_servisi

api_arayuzu = Blueprint("api", __name__)
sayfa_arayuzu = Blueprint("sayfa", __name__)

# 1) Karşılama sayfası
@sayfa_arayuzu.route("/")
def anasayfa():
    return render_template("index.html")

# 2) Yönetim paneli
@sayfa_arayuzu.route("/panel")
def panel():
    return render_template("dashboard.html")

# 3) Sohbet (AI servisi)
@api_arayuzu.route("/sohbet", methods=["POST"])
def sohbet_et():
    veri = request.json
    mesaj = veri.get("mesaj")
    gecmis = veri.get("gecmis", [])

    if not mesaj:
        return jsonify({"basari": False, "hata": "Mesaj boş olamaz."}), 400

    try:
        yanit = yapay_zeka_servisi.yanit_uret(mesaj, gecmis)
        return jsonify({"basari": True, "cevap": yanit})
    except Exception as e:
        return jsonify({"basari": False, "hata": str(e)}), 503

# 4) Yeni müşteri kaydı
@api_arayuzu.route("/adaylar", methods=["POST"])
def aday_ekle():
    veri = request.json
    musteri_adayi_ekle(veri["isim"], veri["telefon"], veri["mesaj"])
    return {"basari": True, "mesaj": "Kayıt eklendi"}

# 5) Tüm müşteri adaylarını listeleme
@api_arayuzu.route("/adaylar", methods=["GET"])
def adaylari_getir():
    kayitlar = tum_adaylari_getir()
    return jsonify(kayitlar)

# 6) Sağlık kontrolü
@api_arayuzu.route("/saglik-durumu", methods=["GET"])
def saglik_durumu():
    return {"durum": "çalışıyor"}
