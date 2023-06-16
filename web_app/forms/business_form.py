from flask_wtf import FlaskForm
from wtforms import (
    IntegerField, StringField, 
    SubmitField, TextAreaField, URLField, 
    BooleanField
    )
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import (
    InputRequired
    )


class Business_Form(FlaskForm):


    id = IntegerField("id", validators=[InputRequired()])


    name = StringField("Business Name")


    business_desc = TextAreaField("Description")


    sold = BooleanField("Sold")


    link = URLField('Link')


    business_image_ = FileField(
        "Business Image",
        validators=[ 
            FileRequired(), 
            FileAllowed(
                ['jpg', 'png', 'webp'], 'images only!')
                ])
    

    submit = SubmitField("Submit",  validators=[InputRequired()])
    delete = StringField("Type in 'Delete' to delete entity: ")

