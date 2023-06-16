from web_app.models import (
    Client,
    Employee,
    Business,
    Real_Estate
    )


# GETTING MODEL BASED UPON JS USER DATA POST REQUEST (selected_form)

def get_model(selected_form: str, db_model_data=None):

    get_model_dict = {
    'clients' : Client,
    'employees' : Employee,
    'businesses' : Business,
    'real_estate' : Real_Estate
    }

    # NO PREFILLED MODEL WITH CURRENT DB DATA, RETURNED FOR ADD ROUTE

    if not db_model_data:
        return get_model_dict[selected_form]
    
    # --------------------------------------
    

    # PREFILLED MODEL WITH CURRENT DB DATA, RETURNED FOR EDIT ROUTE

    return get_model_dict[selected_form](**db_model_data) 

    # --------------------------------------