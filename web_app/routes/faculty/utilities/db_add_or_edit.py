from flask import current_app
from dataclasses import asdict


# DATABASE ADDITION OR EDITING ENTITY HELPER FUNCTION

def db_add_or_edit(selected_form: str, mod_selection: str, model, prev_id : int):

    if mod_selection == 'add':
        current_app.db[selected_form].insert_one(
            {'info' : asdict(model)})

    if mod_selection == 'edit':
        current_app.db[selected_form].update_one(
            {'info.id' : prev_id}, 
            {"$set" : { 'info' : asdict(model)}})