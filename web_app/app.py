import os
from dataclasses import asdict
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
client = MongoClient(os.environ.get("MONGODB_URI"))
app.db = client.get_default_database()
app.secret_key = os.environ.get('SECRET_KEY', 'dev')



# homepage route


@app.route("/")
def index():
    return render_template("index.html")

# about us route


@app.route("/our_team")
def our_team():
    return render_template(
        "/about_us/our_team.html",
        employees=app.db.employees.find({}, {"_id": False}))


@app.route("/our_company_mindset")
def our_company_mindset():
    return render_template("/about_us/our_company_mindset.html")

# listings route


@app.route('/business_listings')
def business_listings():
    return render_template(
        "/listings/business_listings.html",
        businesses=app.db.businesses.find({}, {"_id": False})
        )


@app.route('/real-estate_listings')
def real_estate_listings():
    return render_template("/listings/real_estate_listings.html")

# login page


@app.route("/login")
def login():
    return render_template("resources/login.html")


# add or edit entities

@app.route('/add_or_edit', methods=["GET", "POST"])
def add_or_edit():
    if request.method == "POST":
        collection = request.form.get("javascript_data")
        entities = app.db[collection].find({})

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
        selected_form_edit = request.form.get('select--edit')
        selected_form_add = request.form.get('select--add')
        entity_id = request.form.get('entities_to_edit') 
        # ---------------------------------------------------


        if ((selected_form_add == '#' 
            and selected_form_edit == '#') 
            or ( entity_id == '#' and selected_form_edit != '#' )):
            return redirect( url_for('add_or_edit') ) # NEEDS ERROR MESSAGE ----------
        
        
        # MODIFICATION SELECTION IS "add"
        if mod_selection == 'add':
            return redirect(url_for(
                'add',
                selected_form_add=selected_form_add,
                mod_selection=mod_selection
                ))
        
        # MODIFICATION SELECTION IS "edit"
        elif mod_selection == 'edit':
            return redirect(url_for(
                'edit', 
                entity_id=entity_id,
                selected_form_edit=selected_form_edit,
                mod_selection=mod_selection
                ))

        else:
            return redirect(url_for('add_or_edit')) # NEEDS ERROR MESSAGE --------
        



def get_form(
        selected_form: str, 
        model : 
        Client | 
        Employee | 
        Business | 
        Real_Estate
        =None ) -> (
    Client_Form | 
    Employee_Form | 
    Business_Form | 
    Real_Estate_Form
    ):
    
    get_form_dict = {
    'clients' : Client_Form,
    'employees' : Employee_Form,
    'businesses' : Business_Form,
    'real_estate' : Real_Estate_Form
    }


    return get_form_dict[selected_form](obj=model)


def get_model(selected_form: str, db_model_data=None):

    get_model_dict = {
    'clients' : Client,
    'employees' : Employee,
    'businesses' : Business,
    'real_estate' : Real_Estate
    }

    # if there is no form data (add entity selection guard)
    if not db_model_data:
        return get_model_dict[selected_form]
    # --------------------------------------
    
    return get_model_dict[selected_form](**db_model_data)


def db_add_or_edit(selected_form: str, mod_selection: str, model, prev_id : int):

    if mod_selection == 'add':
        app.db[selected_form].insert_one(
            {'info' : asdict(model)})

    if mod_selection == 'edit':
        app.db[selected_form].update_one(
            {'info.id' : prev_id}, 
            {"$set" : { 'info' : asdict(model)}})
        



def update_model(selected_form: str, mod_selection: str, form, prev_id: int):
    
    if selected_form == 'employees':
        
        model = Employee(
        form.id.data,
        form.name.data,
        form.cell_number.data,
        form.email.data,
        form.background.data,
        form.positions.data,
        form.linkedin.data
        )
        db_add_or_edit(selected_form, mod_selection, model, prev_id)

    elif selected_form == 'clients':
        
        model = Client(
        form.id.data,
        form.name.data,
        form.business_name.data,
        form.email.data,
        form.cell_number.data,
        form.website_address.data,
        form.annual_revenue.data,
        form.questions_or_comments.data
        )

        db_add_or_edit(selected_form, mod_selection, model, prev_id)
        
    
    elif selected_form == 'businesses':
        
        model = Business(
        form.id.data,
        form.name.data,
        form.business_desc.data,
        form.link.data,
        form.sold.data
        )
        db_add_or_edit(selected_form, mod_selection, model, prev_id)
    
    
    elif selected_form == 'real_estate':
        
        model = Real_Estate(
        form.id.data,
        form.name.data,
        form.price.data,
        form.location.data,
        form.rooms.data,
        form.baths.data,
        form.sqft.data,
        form.sold.data
        )
        db_add_or_edit(selected_form, mod_selection, model, prev_id)

    
        


@app.route("/add_or_edit/selection/add", methods=["GET", "POST"])
def add():
    mod_selection = request.args.get('mod_selection')
    selected_form_add = request.args.get('selected_form_add') 
    form = get_form(selected_form_add)

    if form.validate_on_submit():
        update_model(selected_form_add, mod_selection, form, None)
        return redirect(url_for('add_or_edit')) # SUCCESS MESSAGE NEEDED --------------------
    
    return render_template(
                '/web_app_mods/add.html',
                form=form,
                selected_form_add = selected_form_add,
                mod_selection=mod_selection
            )
        


@app.route("/add_or_edit/selection/edit", methods=["GET", "POST"])
def edit():

    # DATA FROM /add_or_edit/selection ENDPOINT
    mod_selection : str = request.args.get('mod_selection')
    selected_form_edit : str = request.args.get('selected_form_edit')
    entity_id = int(request.args.get('entity_id')) 
    # --------------------------------------------
        
    # CURRENT DATA FROM MONGODB
    entity_data =(
        app.db[selected_form_edit]
        .find({'info.id' : entity_id})[0]['info']
        )
    
    
    model = get_model(
        selected_form_edit, 
        db_model_data=entity_data
        )
    
    form = get_form(
        selected_form_edit, 
        model
        )

    if form.validate_on_submit():
        if form.delete.data == 'Delete':
            app.db[selected_form_edit].delete_many({'info.id' : entity_id})
             
            

        update_model(selected_form_edit, mod_selection, form, entity_id)
        return redirect(url_for('add_or_edit')) # SuCCESS MESSAGE NEEDED ----------------



    return render_template(
            '/web_app_mods/edit.html',
            form=form,
            model=model,
            entity_id=entity_id,
            selected_form_edit=selected_form_edit,
            mod_selection=mod_selection
        )

    



if __name__ == "__main__":
    app.run(debug=True)
