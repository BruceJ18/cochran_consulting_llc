from flask_wtf import FlaskForm
from wtforms import (
    IntegerField, StringField, 
    SubmitField, URLField, 
    BooleanField
    )
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import (
    InputRequired
    )


class Real_Estate_Form(FlaskForm):


    id = IntegerField("id", validators=[InputRequired()])


    name = StringField("Name", validators=[InputRequired()])


    price = StringField("Price")


    location = StringField("Location")


    rooms = IntegerField("Rooms")


    baths = IntegerField("Baths")


    sqft = IntegerField("Sqft")


    sold = BooleanField("Sold")


    link = URLField('Link')


    home_image_ = FileField(
        "Home Image",
        validators=[ 
            FileAllowed(
                ['jpg', 'png', 'webp'], 'images only!')
                ])    
    
    
    submit = SubmitField("Submit",  validators=[InputRequired()])
    delete = StringField("Type in 'Delete' to delete entity: ")
