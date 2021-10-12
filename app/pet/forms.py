from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired

class AddPetForm(FlaskForm):
    ''' Form for adding a new animal '''
    name = StringField('Name:', validators=[InputRequired()])
    animal_id = SelectField('Animal:', validators=[InputRequired()])
    submit = SubmitField('Add animal')

class EditPetForm(AddPetForm):
    ''' Form for editing an existing animal '''
    submit = SubmitField('Save changes')
