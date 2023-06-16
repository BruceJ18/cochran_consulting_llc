from flask import Blueprint

# --------------- RESOURCES BLUEPRINT -------------------

resources_bp = Blueprint(
    'resources', 
    __name__, 
    template_folder='templates', 
    static_folder='static'
    )

from web_app.routes.resources import resources_routes




