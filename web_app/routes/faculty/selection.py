from flask import request, redirect, url_for

from web_app.routes.faculty import faculty_bp


#-------------------- SELECTION ROUTES ------------------------

@faculty_bp.post("/add_or_edit/selection")
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
            return redirect( url_for('faculty.add_or_edit') ) # NEEDS ERROR MESSAGE ----------
        
        
        # SELECTED MODIFICATION IS "add"
        if mod_selection == 'add':
            return redirect(url_for(
                'faculty.add',
                selected_form_add=selected_form_add,
                mod_selection=mod_selection
                ))
        
        # SELECTED MODIFICATION  IS "edit"
        elif mod_selection == 'edit':
            return redirect(url_for(
                'faculty.edit', 
                entity_id=entity_id,
                selected_form_edit=selected_form_edit,
                mod_selection=mod_selection
                ))

        else:
            return redirect(url_for('faculty.add_or_edit')) # NEEDS ERROR MESSAGE --------
        
