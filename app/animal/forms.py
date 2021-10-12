from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class AddAnimalForm(FlaskForm):
    ''' Form for adding a new animal '''
    name = StringField('Name:', validators=[InputRequired()])
    submit = SubmitField('Add animal')

class EditAnimalForm(AddAnimalForm):
    ''' Form for editing an existing animal '''
    submit = SubmitField('Save changes')
