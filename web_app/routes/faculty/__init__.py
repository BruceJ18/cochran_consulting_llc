from flask import Blueprint


# --------------- FACULTY BLUEPRINT -------------------

faculty_bp = Blueprint(
    'faculty',
    __name__,
    template_folder='templates',
    static_folder='static'
    )


# IMPORT ROUTES

from web_app.routes.faculty import login, add_or_edit, selection, add, edit