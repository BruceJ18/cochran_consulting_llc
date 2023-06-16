from flask import (
    request, 
    render_template, 
    redirect, url_for
    )
from web_app.routes.faculty.utilities import (
    get_form,
    update_model
)
from web_app.routes.faculty import faculty_bp


#-------------------- ADD ROUTE ------------------------


@faculty_bp.route("/add_or_edit/selection/add", methods=["GET", "POST"])
def add():

    mod_selection = request.args.get('mod_selection')
    selected_form_add = request.args.get('selected_form_add') 
    form = get_form(selected_form_add)



    if form.validate_on_submit():

        update_model(selected_form_add, mod_selection, form, None)

        return redirect(url_for('faculty.add_or_edit')) # SUCCESS MESSAGE NEEDED --------------------
    


    return render_template(
                'faculty/web_app_mods/add.html',
                form=form,
                selected_form_add = selected_form_add,
                mod_selection=mod_selection
            )
        
