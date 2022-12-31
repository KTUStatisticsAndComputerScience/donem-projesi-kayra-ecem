from .ma import ma
from vt import Kargo, Sube, Kisi, Sehir

class KargoSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Kargo
        include_fk = True
        load_instance = True

class SubeSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sube
        include_fk = True

class KisiSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Kisi
        load_instance = True

class SehirSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sehir