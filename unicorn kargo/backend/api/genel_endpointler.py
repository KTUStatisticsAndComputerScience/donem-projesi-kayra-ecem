from flask import Blueprint, request, jsonify, json

from vt import vt

def genel_endpoint_olustur(isim, vt_sinifi, sema_sinifi):
    bp = Blueprint(isim, __name__)
    @bp.route('/', methods=['GET'])
    def tumu():
        sorgu = vt.session.query(vt_sinifi)
        if 'sorgu' in request.args:
            talep = request.args['sorgu']
            talep_obj = json.loads(talep)
        sema = sema_sinifi()
        return sema.dump(sorgu, many=True)
    @bp.route('/<int:id>', methods=['GET'])
    def detay(id):
        data = vt.get_or_404(vt_sinifi, id)
        sema = sema_sinifi()
        return sema.dump(data)
    @bp.route('/from/<int:id>/<foreignkey_name>', methods=['GET'])
    def ara(id, foreignkey_name):
        data = vt.session.query(vt_sinifi).filter_by(**{foreignkey_name: id}).all()
        sema = sema_sinifi()
        return sema.dump(data, many=True)

    @bp.route('/', methods=['POST'])
    def ekle():
        bilgiler = request.json
        yeni = vt_sinifi(**bilgiler)
        vt.session.add(yeni)
        vt.session.commit()
        sema = sema_sinifi()
        return sema.dump(yeni)
    @bp.route('/<int:id>', methods=['PUT', 'PATCH'])
    def guncelle(id):
        kayit = vt.get_or_404(vt_sinifi, id)
        kayit_bilgileri = request.json
        sema = sema_sinifi()
        guncel_kayit = sema.load(kayit_bilgileri, instance=kayit, session=vt.session)
        vt.session.commit()
        return sema.dump(guncel_kayit)
    @bp.route('/<int:id>', methods=['DELETE'])
    def sil(id):
        kayit = vt.get_or_404(vt_sinifi, id)
        vt.session.delete(kayit)
        vt.session.commit()
        return jsonify({'sonuc': 'TAMAM'})
    return bp