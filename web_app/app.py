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
from web_app.models import Employee

load_dotenv()

app = Flask(__name__)
client = MongoClient("mongodb+srv://brucej18:illescio369@cluster0.5bjmfpv.mongodb.net/")
app.db = client.cochran_consulting_data



@app.context_processor
def inject_forms():
    forms = [
    Client_Form(),
    Employee_Form(),
    Business_Form(),
    Real_Estate_Form()
    ]
    return dict(forms=forms)

app.config['SECRET_KEY'] = 'any secret string'
# homepage route

@app.route("/")
def index():
    return render_template("index.html")

#about us routes

@app.route("/our_team")
def our_team():
    return render_template(
        "/about_us/our_team.html", 
        employees=app.db.employees.find({}, {"_id": False}))

@app.route("/mindset")
def mindset():
    return render_template("/about_us/mindset.html")

#listings routes

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



@app.post("/add_or_edit/selected")
def selected():
    if request.method == "POST":



        mod_selection = request.form.get('add_or_edit')
        form_type_add = request.form.get('select--add')
        form_type_edit = request.form.get('select--edit')

        entity_id = int( request.form.get('entities_to_edit') ) if request.form.get('entities_to_edit') != '#' else '#'

        if mod_selection == 'add':
            return render_template(
                '/web_app_mods/add.html', 
                form_type_add=form_type_add
                )
        elif mod_selection == 'edit':    
            employee = Employee(**app.db[form_type_edit]
                      .find({})[entity_id]['info']
                      )
            

            return render_template(
                '/web_app_mods/edit.html', 
                form_type_edit=form_type_edit
                
                )
        else:
            return redirect(url_for('add_or_edit'))



# for form in inject_forms()["forms"]:
#         if form.validate_on_submit():
#            pass
            

if __name__ == "__main__":
    app.run(debug=True)