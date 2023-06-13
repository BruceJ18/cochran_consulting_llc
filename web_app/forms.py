from flask_wtf import FlaskForm
from wtforms import (
    IntegerField, StringField, 
    SubmitField, EmailField, 
    TextAreaField, URLField, 
    BooleanField, PasswordField
    )
from wtforms.validators import InputRequired, NumberRange, Length, Email

class Client_form_index(FlaskForm):
    name = StringField("Client Name", validators=[InputRequired()])
    business_name = StringField("Business Name",  validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired("Please enter your email address."), Email()])
    cell_number = IntegerField("Cell",  validators=[InputRequired()])
    website_address = StringField("Website Address", validators=[InputRequired()])
    annual_revenue = IntegerField(
        "Annual Revenue",  
        validators=[
        InputRequired(), 
        NumberRange(
        min=500000, 
        max=50000000, 
        message="Only companies with annual revenues between $500,000 to $50,000,000"
        )])
    questions_or_comments = TextAreaField("Questions or Comments", validators=[InputRequired()])
    submit = SubmitField("Submit")
    delete = StringField("Type in 'Delete' to delete entity: ")


class Client_Form(Client_form_index):
    id = IntegerField("id", validators=[InputRequired()])
    
    

class StringListField(TextAreaField):

    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        if valuelist and valuelist[0]:
            self.data = [ line.strip() for line in valuelist[0].split("\n") ]
        else:
            self.data = ''


class Employee_Form(FlaskForm):
    id = IntegerField("id", validators=[InputRequired()])
    name = StringField("Employee Name:",  validators=[InputRequired()])
    cell_number = StringField("Cell:")
    email = EmailField("Email:",  validators=[InputRequired(), Email()])
    background = TextAreaField("Background:", validators=[Length(max=244)])
    positions = StringListField("Positions:")
    linkedin = URLField("Linkedin:")
    submit = SubmitField("Submit")
    delete = StringField("Type in 'Delete' to delete entity: ")


class Business_Form(FlaskForm):
    id = IntegerField("id", validators=[InputRequired()])
    name = StringField("Business Name")
    business_desc = TextAreaField("Description")
    sold = BooleanField("Sold")
    link = URLField('Link')
    submit = SubmitField("Submit",  validators=[InputRequired()])
    delete = StringField("Type in 'Delete' to delete entity: ")



class Real_Estate_Form(FlaskForm):
    id = IntegerField("id", validators=[InputRequired()])
    price = StringField("Price")
    location = StringField("Location")
    rooms = IntegerField("Rooms")
    baths = IntegerField("Baths")
    sqft = IntegerField("Sqft")
    sold = BooleanField("Sold")
    link = URLField('Link')
    submit = SubmitField("Submit",  validators=[InputRequired()])
    delete = StringField("Type in 'Delete' to delete entity: ")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")
