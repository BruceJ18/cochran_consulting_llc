from flask import Blueprint


# --------------- LISTINGS BLUEPRINT -------------------

listings_bp = Blueprint(
    'listings', 
    __name__, 
    template_folder='templates', 
    static_folder='static'
    )


# IMPORT ROUTES

from web_app.routes.listings import basic_listings_routes