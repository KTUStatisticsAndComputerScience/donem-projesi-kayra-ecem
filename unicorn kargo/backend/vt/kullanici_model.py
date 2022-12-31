import bcrypt

from vt.baglanti import vt

class Kullanici(vt.Model):
    id = vt.Column(vt.Integer, primary_key=True)
    email = vt.Column(vt.String(255))
    sifre = vt.Column(vt.String(255))

    def sifre_ata(self, sifre):
        self.sifre = bcrypt.hashpw(sifre.encode("utf-8"), bcrypt.gensalt(10))

    def sifre_kontrol(self, sifre):
        return bcrypt.checkpw(sifre.encode("utf-8"), self.sifre.endcode("utf-8"))