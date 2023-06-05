import json
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)
from pymongo import MongoClient
from dotenv import load_dotenv
from web_app.forms import (
    Client_Form,
    Employee_Form,
    Business_Form,
    Real_Estate_Form,
)
from web_app.models import (
    Client,
    Employee,
    Business,
    Real_Estate
    )

load_dotenv()

app = Flask(__name__)
client = MongoClient(
    "mongodb+srv://brucej18:illescio369@cluster0.5bjmfpv.mongodb.net/")
app.db = client.cochran_consulting_data




app.config['SECRET_KEY'] = 'any secret string'
# homepage route


@app.route("/")
def index():
    return render_template("index.html")

# about us routes


@app.route("/our_team")
def our_team():
    return render_template(
        "/about_us/our_team.html",
        employees=app.db.employees.find({}, {"_id": False}))


@app.route("/mindset")
def mindset():
    return render_template("/about_us/mindset.html")

# listings routes


@app.route('/business_listings_1')
def business_listings_1():
    return render_template("/listings/business_listings_1.html")


@app.route('/real-estate_listings')
def real_estate_listings():
    return render_template("/listings/real-estate_listings.html")

# login page


@app.route("/login")
def login():
    return render_template("resources/login.html")


# add or edit entities

@app.route('/add_or_edit', methods=["GET", "POST"])
def add_or_edit():
    if request.method == "POST":
        collection = request.form.get("javascript_data")
        entities = app.db[collection].find({}, {"_id": False})

        return render_template(
            "/web_app_mods/add_or_edit.html",
            entities=entities
        )

    return render_template(
        "/web_app_mods/add_or_edit.html"

    )


@app.post("/add_or_edit/selection")
def selection():
    if request.method == "POST":

        # add_or_edit.js POST REQUEST PAYLOAD DATA
        mod_selection = request.form.get('add_or_edit')
        entity_id = request.form.get('entities_to_edit') 
        selected_form_edit = request.form.get('select--edit')
        selected_form_add = request.form.get('select--add')

        if (selected_form_add == '#' 
            and selected_form_edit == '#' 
            or entity_id == '#'):
            return redirect( url_for('add_or_edit') ) # NEEDS ERROR MESSAGE

        if mod_selection == 'add':
            return redirect(url_for(
                'add', 
                selected_form_add=selected_form_add 
                ))

        elif mod_selection == 'edit':
            return redirect(url_for(
                'edit', 
                entity_id=entity_id,
                selected_form_edit=selected_form_edit 
                ))

        else:
            return redirect(url_for('add_or_edit'))
        



def get_form(selected_form: str, entity=None):
    
    get_form_dict = {
    'clients' : Client_Form,
    'employees' : Employee_Form,
    'businesses' : Business_Form,
    'real_estate' : Real_Estate_Form
    }

    return get_form_dict[selected_form](obj=entity)


def get_model(selected_form: str, entity_data=None):

    get_form_dict = {
    'clients' : client,
    'employees' : Employee,
    'businesses' : Business,
    'real_estate' : Real_Estate
    }
    if not entity_data:
        return get_form_dict[selected_form]
    
    return get_form_dict[selected_form](**entity_data)
        
        
@app.route("/add_or_edit/selection/add", methods=["GET", "POST"])
def add():
    selected_form_add = request.args.get('selected_form_add')

    form = get_form(selected_form_add)


    return render_template(
                '/web_app_mods/add.html',
                selected_form_add=selected_form_add,
                form=form
            )



@app.route("/add_or_edit/selection/edit", methods=["GET", "POST"])
def edit():

    # DATA FROM add_or_edit/selection ENDPOINT
    selected_form_edit = request.args.get('selected_form_edit')
    entity_id = int(request.args.get('entity_id')) 
    # --------------------------------------------
        

    entity_data =(
        app.db[selected_form_edit]
        .find({})[entity_id - 1]['info']
        )
    
    entity = get_model(
        selected_form_edit, 
        entity_data=entity_data
        )
    
    form = get_form(
        selected_form_edit, 
        entity=entity
        )


    if form.validate_on_submit():
        pass


    return render_template(
            '/web_app_mods/edit.html',
            selected_form_edit=selected_form_edit,
            form=form
        )



if __name__ == "__main__":
    app.run(debug=True)
