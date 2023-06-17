from flask import Blueprint, render_template
from web_app.forms import Client_Form_Index
from web_app.routes.listings import listings_bp
from web_app.routes.resources import resources_bp
from web_app.routes.about_us import about_us_bp
from web_app.routes.faculty import faculty_bp


# -------------- INDEX BLUEPRINT ------------------

index_bp = Blueprint(
    'index',
    __name__,
    template_folder='templates',
    static_folder='static'
)


# INDEX ROUTE

@index_bp.route("/")
def index():
    client_form = Client_Form_Index()
    return render_template("index.html", client_form=client_form)
