import os
from flask import Flask
from dotenv import load_dotenv
from api import api
from export import ma
from vt import *
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
vt.init_app(app)
ma.init_app(app)
migrate.init_app(app, vt)
CORS(app)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

app.register_blueprint(api, url_prefix="/api")

if __name__ == '__main__':
    app.run()
