import os
from passlib.hash import pbkdf2_sha256
from dataclasses import asdict
from flask import (
    Flask,
    flash,
    render_template,
    request,
    redirect,
    session,
    url_for
)
from pymongo import MongoClient
from dotenv import load_dotenv
from web_app.forms import (
    Client_Form,
    Client_Form_Index,
    Employee_Form,
    Business_Form,
    Real_Estate_Form,
    LoginForm
)
from web_app.models import (
    Client,
    Employee,
    Business,
    Real_Estate,
    User
    )
from web_app.routes import (
    listings_bp, 
    resources_bp, 
    about_us_bp, 
    faculty_bp
    )


load_dotenv()

app = Flask(__name__)

app.register_blueprint(about_us_bp)
app.register_blueprint(listings_bp)
app.register_blueprint(resources_bp)
app.register_blueprint(faculty_bp)


client = MongoClient(os.environ.get("MONGODB_URI"))
app.db = client.get_default_database()

app.secret_key = os.environ.get('SECRET_KEY')
UPLOAD_FOLDER = 'web_app/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# homepage route


@app.route("/")
def index():

    client_form = Client_Form_Index()

    return render_template("index.html", client_form=client_form)


# def get_form(
#         selected_form: str, 
#         model : 
#         Client | 
#         Employee | 
#         Business | 
#         Real_Estate
#         = None) -> (
#     Client_Form | 
#     Employee_Form | 
#     Business_Form | 
#     Real_Estate_Form
#     ):
    
#     get_form_dict = {
#     'clients' : Client_Form,
#     'employees' : Employee_Form,
#     'businesses' : Business_Form,
#     'real_estate' : Real_Estate_Form
#     }


#     return get_form_dict[selected_form](obj=model)


# def get_model(selected_form: str, db_model_data=None):

#     get_model_dict = {
#     'clients' : Client,
#     'employees' : Employee,
#     'businesses' : Business,
#     'real_estate' : Real_Estate
#     }

#     # if there is no form data (add entity selection guard)
#     if not db_model_data:
#         return get_model_dict[selected_form]
#     # --------------------------------------
    
#     return get_model_dict[selected_form](**db_model_data)


# def db_add_or_edit(selected_form: str, mod_selection: str, model, prev_id : int):

#     if mod_selection == 'add':
#         app.db[selected_form].insert_one(
#             {'info' : asdict(model)})

#     if mod_selection == 'edit':
#         app.db[selected_form].update_one(
#             {'info.id' : prev_id}, 
#             {"$set" : { 'info' : asdict(model)}})
        




# def update_model(selected_form: str, mod_selection: str, 
#                  form:
#                 Client_Form | 
#                 Employee_Form | 
#                 Business_Form | 
#                 Real_Estate_Form
#                  , prev_id: int):
    
#     if selected_form == 'employees':

       

#         model = Employee(
#         form.id.data,
#         form.name.data,
#         form.cell_number.data,
#         form.email.data,
#         form.background.data,
#         form.positions.data,
#         form.linkedin.data
#         )
        
        
#         if form.employee_image_.data != None:
#             file = request.files['employee_image_']
#             name_id = form.employee_image_.name + str(form.id.data) + '.png'
#             folder = app.config['UPLOAD_FOLDER'] + '/our_team/'
#             file.save(os.path.join(folder, name_id))
        
        
        
#         db_add_or_edit(selected_form, mod_selection, model, prev_id)

#     elif selected_form == 'clients':

        
#         model = Client(
#         form.id.data,
#         form.name.data,
#         form.business_name.data,
#         form.email.data,
#         form.cell_number.data,
#         form.website_address.data,
#         form.annual_revenue.data,
#         form.questions_or_comments.data
#         )

        
#         db_add_or_edit(selected_form, mod_selection, model, prev_id)
        
    
#     elif selected_form == 'businesses':
        
#         model = Business(
#         form.id.data,
#         form.name.data,
#         form.business_desc.data,
#         form.link.data,
#         form.sold.data
#         )

#         if form.home_image_.data != None:
#             file = request.files['business_image_']
#             name_id = form.business_image_.name + str(form.id.data) + '.png'
#             folder = app.config['UPLOAD_FOLDER'] + '/business_listings/'
#             file.save(os.path.join(folder, name_id))

#         db_add_or_edit(selected_form, mod_selection, model, prev_id)
    
    
#     elif selected_form == 'real_estate':
        
#         model = Real_Estate(
#         form.id.data,
#         form.name.data,
#         form.price.data,
#         form.location.data,
#         form.rooms.data,
#         form.baths.data,
#         form.sqft.data,
#         form.link.data,
#         form.sold.data
#         )
#         if form.home_image_.data != None:
#             file = request.files['home_image_']
#             name_id = form.home_image_.name + str(form.id.data) + '.png'
#             folder = app.config['UPLOAD_FOLDER'] + '/real_estate_listings/'
#             file.save(os.path.join(folder, name_id))
        
#         db_add_or_edit(selected_form, mod_selection, model, prev_id)

    

        


# @app.route("/add_or_edit/selection/add", methods=["GET", "POST"])
# def add():

#     mod_selection = request.args.get('mod_selection')
#     selected_form_add = request.args.get('selected_form_add') 
#     form = get_form(selected_form_add)



#     if form.validate_on_submit():
#         update_model(selected_form_add, mod_selection, form, None)
#         return redirect(url_for('add_or_edit')) # SUCCESS MESSAGE NEEDED --------------------
    
#     return render_template(
#                 'faculty/web_app_mods/add.html',
#                 form=form,
#                 selected_form_add = selected_form_add,
#                 mod_selection=mod_selection
#             )
        


# @app.route("/add_or_edit/selection/edit", methods=["GET", "POST"])
# def edit():

#     # DATA FROM /add_or_edit/selection ENDPOINT
#     mod_selection : str = request.args.get('mod_selection')
#     selected_form_edit : str = request.args.get('selected_form_edit')
#     entity_id = int(request.args.get('entity_id')) 
#     # --------------------------------------------
        
#     # CURRENT DATA FROM MONGODB
#     entity_data =(
#         app.db[selected_form_edit]
#         .find({'info.id' : entity_id})[0]['info']
#         )
    
    
#     model = get_model(
#         selected_form_edit, 
#         db_model_data=entity_data
#         )
    
#     form = get_form(
#         selected_form_edit, 
#         model
#         )

#     if form.validate_on_submit():
#         if form.delete.data == 'Delete':
#             app.db[selected_form_edit].delete_many({'info.id' : entity_id})

#             if selected_form_edit == 'employees':
#                 path = 'our_team/employee_image_' + str(form.id.data) + '.png'
#             elif selected_form_edit == 'businesses':
#                 path = 'business_listings/business_image_' + str(form.id.data) + '.png'
#             elif selected_form_edit == 'real_estate':
#                 path = 'real_estate_listings/home_image_' + str(form.id.data) + '.png'
                
            
            
#             # must change to server path -below ------------------------------------------------------

#             full_path = '/Users/bruce/OneDrive/Documents/cochran_consulting_llc/web_app/static/images/' + path 
#             rel_path = '/static/images/' + path

#             if os.path.exists(full_path):
#                 os.remove( full_path )

#             return redirect(url_for('index')) # no image was given or deleted MESSAGE
            

#         update_model(selected_form_edit, mod_selection, form, entity_id)
#         return redirect(url_for('add_or_edit')) # SuCCESS MESSAGE NEEDED ----------------------------



#     return render_template(
#             'faculty/web_app_mods/edit.html',
#             form=form,
#             model=model,
#             entity_id=entity_id,
#             selected_form_edit=selected_form_edit,
#             mod_selection=mod_selection
#         )

    



if __name__ == "__main__":
    app.run(debug=True)
