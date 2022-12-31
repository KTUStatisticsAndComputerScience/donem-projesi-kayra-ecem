import os

import jwt
from flask import Blueprint, request, jsonify

from vt import Kullanici, vt

kullanici = Blueprint('kullanici', __name__, url_prefix='/kullanici')

@kullanici.route('/kayit', methods=['POST'])
def kayit():
    yeni_kullanici = Kullanici()
    yeni_kullanici.email = request.json['email']
    yeni_kullanici.sifre_ata(request.json['sifre'])
    vt.session.add(yeni_kullanici)
    vt.session.commit()
    return jsonify({"id":yeni_kullanici})

@kullanici.route('/giris', methods=['POST'])
def giris():
    kullanici_giris = vt.session.query(Kullanici).filter_by(email=request.json['email']).first()
    if kullanici_giris is None:
        return jsonify({"hata": "kullanıcı bulunamadı"})
    if kullanici_giris.sifre_kontrol(request.json['sifre']):
        return jsonify({"token" : jwt.encode({"id":f"{kullanici_giris.id}"}, os.getenv("TOKEN"), algorithm="HS256")})

def token_kontrol(fonk):
    @wraps(fonk)
    def yeni_fonksiyon(*args, **kwargs):
        #jwt kontrol
        if 'Yetkilendirme' not in request.headers:
            return jsonify({'hata': 'token bulunamadı'})
        user_id = jwt.decode(request.headers['Yetkilendirme'], os.getenv("JWT_SECRET"), algorithm="HS256")
        fonk(*args, **kwargs)
    return yeni_fonksiyon()