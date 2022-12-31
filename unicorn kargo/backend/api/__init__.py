from flask import Blueprint

from vt import Kargo, Kisi
from export.semalar import KargoSema, KisiSema, SehirSema, SubeSema
from .genel_endpointler import genel_endpoint_olustur
from .hesaplama import hesap

v1 = Blueprint("v1", __name__)
v1.register_blueprint(genel_endpoint_olustur("kargo", Kargo, KargoSema), url_prefix="/kargo")
v1.register_blueprint(genel_endpoint_olustur("kisi", Kisi, KisiSema), url_prefix="/kisi")
v1.register_blueprint(genel_endpoint_olustur("sehir", Kisi, SehirSema), url_prefix="/sehir")
v1.register_blueprint(genel_endpoint_olustur("sube", Kisi, SubeSema), url_prefix="/sube")
v1.register_blueprint(hesap)

api = Blueprint("api", __name__)
api.register_blueprint(v1, url_prefix="/v1")