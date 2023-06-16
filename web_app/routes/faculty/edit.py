import os
from flask import (
    request, 
    render_template, 
    current_app, 
    redirect, url_for
    )
from web_app.routes.faculty import faculty_bp
from web_app.routes.faculty.utilities import (
    update_model,
    get_form,
    get_model
)


#-------------------- EDIT ROUTE ------------------------


@faculty_bp.route("/add_or_edit/selection/edit", methods=["GET", "POST"])
def edit():

    # DATA FROM /add_or_edit/selection ENDPOINT
    mod_selection : str = request.args.get('mod_selection')
    selected_form_edit : str = request.args.get('selected_form_edit')
    entity_id = int(request.args.get('entity_id')) 
    # --------------------------------------------
        
    # CURRENT DATA FROM MONGODB
    entity_data =(
        current_app.db[selected_form_edit]
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

            current_app.db[selected_form_edit].delete_many({'info.id' : entity_id})

            if selected_form_edit == 'employees':
                path = 'our_team/employee_image_' + str(form.id.data) + '.png'

            elif selected_form_edit == 'businesses':
                path = 'business_listings/business_image_' + str(form.id.data) + '.png'

            elif selected_form_edit == 'real_estate':
                path = 'real_estate_listings/home_image_' + str(form.id.data) + '.png'
                
            
            
            # must change to server path -below ------------------------------------------------------

            full_path = '/Users/bruce/OneDrive/Documents/cochran_consulting_llc/web_app/static/images/' + path 


            # CATCH IMAGE ABSENCE

            if os.path.exists(full_path):
                os.remove( full_path )

            return redirect(url_for('index')) # no image was given or deleted MESSAGE
            

        update_model(selected_form_edit, mod_selection, form, entity_id)
        return redirect(url_for('faculty.add_or_edit')) # SuCCESS MESSAGE NEEDED ----------------------------



    return render_template(
            'faculty/web_app_mods/edit.html',
            form=form,
            model=model,
            entity_id=entity_id,
            selected_form_edit=selected_form_edit,
            mod_selection=mod_selection
        )

    