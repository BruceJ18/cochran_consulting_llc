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


# GETTING FORM BASED UPON JS USER DATA POST REQUEST (selected_form)


def get_form(
        selected_form: str, 
        model : 
        Client | 
        Employee | 
        Business | 
        Real_Estate
        = None) -> (
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

    # PREFILLED (EDIT ROUTE) OR EMPTY ( ADD ROUTE, model = NONE ) FORM

    return get_form_dict[selected_form](obj=model)