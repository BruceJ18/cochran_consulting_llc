from flask_wtf import FlaskForm
from wtforms import (
    IntegerField, StringField, 
    SubmitField, EmailField, 
    TextAreaField, URLField
    )
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import (
    InputRequired, 
    Length, Email
    )


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


    employee_image_ = FileField(
        "Employee Image",
        validators=[
            FileAllowed(
                ['jpg', 'png', 'webp'], 'images only!')
                ])
    
    
    submit = SubmitField("Submit")
    delete = StringField("Type in 'Delete' to delete entity: ")
