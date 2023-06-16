from flask import Blueprint


# --------------- RESOURCES BLUEPRINT -------------------

resources_bp = Blueprint(
    'resources',
    __name__, 
    template_folder='templates',
    static_folder='static'
    )


# IMPORT ROUTES

from web_app.routes.resources import basic_resources_routes