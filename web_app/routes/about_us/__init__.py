from flask import Blueprint


# --------------- ABOUT US BLUEPRINT -------------------

about_us_bp = Blueprint(
    'about_us', 
    __name__, 
    template_folder='templates', 
    static_folder='static'
    )


# IMPORT ROUTES

from web_app.routes.about_us import basic_about_us_routes