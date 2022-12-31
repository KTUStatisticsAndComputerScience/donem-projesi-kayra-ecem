from .baglanti import vt

class Kisi(vt.Model):
    kisi_id = vt.Column(vt.Integer, primary_key=True)
    kisi_adi = vt.Column(vt.String(255))
    kisi_soyadi = vt.Column(vt.String(255))
    tel = vt.Column(vt.String(12))
    adres = vt.Column(vt.String(255))

    kargo_alici = vt.relationship("Kargo", backref="gondericiler", foreign_keys="Kargo.alici", cascade="all, delete-orphan")
    kargo_gonderici = vt.relationship("Kargo", backref="alicilar", foreign_keys="Kargo.gonderici", cascade="all, delete-orphan")