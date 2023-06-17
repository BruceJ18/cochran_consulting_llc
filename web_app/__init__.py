import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from web_app.forms import Client_Form_Index
from web_app.routes import (
    listings_bp, 
    resources_bp, 
    about_us_bp, 
    faculty_bp,
    index_bp
    )


# ---------------------- FLASK APP FACTORY -------------------

def create_app():
    

    app = Flask(__name__)

    # PYTHON - DOTENV
    
    load_dotenv()

    #MONGODB CLIENT

    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.get_default_database()

    # ------------------ CONFIG ------------------

    app.secret_key = os.environ.get('SECRET_KEY')
    app.config['UPLOAD_FOLDER'] = os.environ.get('IMAGE_UPLOAD_FOLDER')
    app.config['EMAIL'] = os.environ.get('CLIENT_INFO_EMAIL')
    app.config['PSWRD'] = os.environ.get('CLIENT_INFO_EMAIL_PSWRD')
    app.config['PORT'] = os.environ.get('PORT')



    # ----------- REGISTERED BLUE PRINTS ---------

    app.register_blueprint(index_bp)
    app.register_blueprint(about_us_bp)
    app.register_blueprint(listings_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(faculty_bp)


    return app


if __name__ == '__main__':
    create_app()