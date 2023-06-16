from flask_wtf import FlaskForm
from wtforms import (
    IntegerField, StringField, 
    SubmitField, EmailField, 
    TextAreaField
    )
from wtforms.validators import (
    InputRequired, 
    NumberRange, 
    Email
    )


class Client_Form_Index(FlaskForm):


    name = StringField(
        "Name* :", 
        validators=[InputRequired()])


    business_name = StringField(
        "Business Name* :",  
        validators=[InputRequired()])


    email = EmailField(
        "Email* :", 
        validators=[
            InputRequired("Please enter your email address."), Email()])


    cell_number = IntegerField(
        "Cell* :",  
        validators=[InputRequired()])


    website_address = StringField("Website Address* :", validators=[InputRequired()])


    annual_revenue = IntegerField(
        "Annual Revenue* :",  
        validators=[
        InputRequired(), 
        NumberRange(
        min=500000, 
        max=50000000, 
        message="Only companies with annual revenues between $500,000 to $50,000,000"
        )])
    

    questions_or_comments = TextAreaField(
        "Questions or Comments* :", 
        validators=[InputRequired()])

    submit = SubmitField("Submit")
    


class Client_Form(Client_Form_Index):
    id = IntegerField("id", validators=[InputRequired()])
    delete = StringField("Type in 'Delete' to delete entity: ")
    

