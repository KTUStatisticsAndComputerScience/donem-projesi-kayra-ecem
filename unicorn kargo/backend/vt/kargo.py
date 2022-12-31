from .baglanti import vt
from sqlalchemy import ForeignKey

class Kargo(vt.Model):
    kargo_id = vt.Column(vt.Integer, primary_key=True)
    kargo_adi = vt.Column(vt.String(255))
    alici = vt.Column(vt.Integer, ForeignKey("kisi.kisi_id"))
    gonderici = vt.Column(vt.Integer, ForeignKey("kisi.kisi_id")) #?????
    agirlik = vt.Column(vt.Integer)
