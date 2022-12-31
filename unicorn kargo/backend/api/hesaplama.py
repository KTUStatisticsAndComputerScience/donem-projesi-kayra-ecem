from flask import Blueprint, jsonify

hesap = Blueprint('hesap', __name__, url_prefix='/hesap')

@hesap.route("/agirlik/<int:agirlik>/<int:birim_fiyat>", methods=['GET'])
def kargo_hesapla(agirlik, birim_fiyat):
    sonuc = agirlik * birim_fiyat
    return jsonify({"sonuc":sonuc})