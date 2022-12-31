from .baglanti import vt
from sqlalchemy import ForeignKey

class Sehir(vt.Model):
    sehir_id = vt.Column(vt.Integer, primary_key=True)
    sehir_adi = vt.Column(vt.String(255))
    sube = vt.relationship("Sube", backref="subeler", cascade="all, delete-orphan")