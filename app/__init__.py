from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)

   
    app.config.from_object('app.config.Config')

   
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client['Corider']


    from app.routes import main
    app.register_blueprint(main)

    return app
