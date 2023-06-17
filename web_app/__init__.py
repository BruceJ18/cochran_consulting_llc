import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from web_app.forms import Client_Form_Index
from web_app.routes import (
    listings_bp, 
    resources_bp, 
    about_us_bp, 
    faculty_bp
    )


# ---------------------- FLASK APP FACTORY -------------------

def create_app():
    

    app = Flask(__name__)

    # PYTHON - DOTENV
    load_dotenv()

    #MONGODB CLIENT
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.get_default_database()

    # SECRET KEY FOR SESSION
    app.secret_key = os.environ.get('SECRET_KEY')

    # UPLOAD FOLDER FOR FILE (IMAGE) USER INPUT
    
    app.config['UPLOAD_FOLDER'] = os.environ.get('IMAGE_UPLOAD_FOLDER')


     # --------------- INDEX ROUTE ---------------

    @app.route("/")
    def index():
        client_form = Client_Form_Index()
        return render_template("index.html", client_form=client_form)


    # ----------- REGISTERED BLUE PRINTS ---------

    app.register_blueprint(about_us_bp)
    app.register_blueprint(listings_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(faculty_bp)


    return app


if __name__ == '__main__':
    create_app()