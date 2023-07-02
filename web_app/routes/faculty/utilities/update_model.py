import os
from flask import request, current_app
from web_app.forms import (
    Client_Form,
    Employee_Form,
    Business_Form,
    Real_Estate_Form
)
from web_app.models import (
    Client,
    Employee,
    Business,
    Real_Estate
    )
from web_app.routes.faculty.utilities.db_add_or_edit import db_add_or_edit




def update_model(selected_form: str, mod_selection: str, 
                 form:
                Client_Form | 
                Employee_Form | 
                Business_Form | 
                Real_Estate_Form
                 , prev_id: int):
    
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
        
        
        if form.employee_image_.data is not None:
            file = request.files['employee_image_']
            name_id = form.employee_image_.name + str(form.id.data) + '.png'
            folder = current_app.config['UPLOAD_FOLDER'] + '/our_team/'
            file.save(os.path.join(folder, name_id))
        
        
        
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

        if form.home_image_.data is not None:
            file = request.files['business_image_']
            name_id = form.business_image_.name + str(form.id.data) + '.png'
            folder = current_app.config['UPLOAD_FOLDER'] + '/business_listings/'
            file.save(os.path.join(folder, name_id))

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
        form.link.data,
        form.sold.data
        )
        if form.home_image_.data is not None:
            file = request.files['home_image_']
            name_id = form.home_image_.name + str(form.id.data) + '.png'
            folder = current_app.config['UPLOAD_FOLDER'] + '/real_estate_listings/'
            file.save(os.path.join(folder, name_id))
        
        db_add_or_edit(selected_form, mod_selection, model, prev_id)