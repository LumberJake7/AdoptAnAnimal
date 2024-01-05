from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name can't be blank")])
    species = StringField("Species", validators=[InputRequired(message="We need to know it's species")])
    photo_url = StringField("Photo URL")
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)] )
    notes = StringField("Notes")
    available = BooleanField("Is it available?")
    
class EditPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name can't be blank")])
    species = StringField("Species", validators=[InputRequired(message="We need to know it's species")])
    photo_url = StringField("Photo URL")
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)] )
    notes = StringField("Notes")
    available = BooleanField("Is it available?")