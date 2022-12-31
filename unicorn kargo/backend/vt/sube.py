from .baglanti import vt
from sqlalchemy import ForeignKey

class Sube(vt.Model):
    sube_id = vt.Column(vt.Integer, primary_key=True)
    sube_sehiri = vt.Column(vt.Integer, ForeignKey("sehir.sehir_id"))
    sube_adi = vt.Column(vt.String(255))
    sube_tel = vt.Column(vt.String(12))

