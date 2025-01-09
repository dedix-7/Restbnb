#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    SubmitField,
    SelectField, EmailField,
    PasswordField, BooleanField
)
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError
)
from flask_wtf.file import FileField, FileAllowed
from estate_finder.models import User


class PropertyForm(FlaskForm):
    propertyImage = FileField(
             'Property Image URL', validators=[FileAllowed(['jpg', 'png'])])
    propertyStatus = SelectField(
             'Property Status', choices=[
                  ('For Rent', 'For Rent'),
                  ('For Sale', 'For Sale')], validators=[DataRequired()])
    property_type = SelectField(
             'Property Type', choices=[
                  ('Apartment', 'Apartment'),
                  ('Villa', 'Villa'),
                  ('Home', 'Home'),
                  ('Building', 'Building'),
                  ('Office', 'Office'),
                  ('Townhouse', 'Townhouse'),
                  ('Shop', 'Shop'),
                  ('Garage', 'Garage')], validators=[DataRequired()])
    propertyPrice = StringField('Property Price(KSH)', validators=[DataRequired()])
    propertyLocation = SelectField(
             'Property Type', choices=[
                  ('Ruiru', 'Ruiru'),
                  ('Westlands', 'Westlands'),
                  ('Karen', 'Karen'),
                  ('Kilimani', 'Kilimani'),
                  ('Muthaiga', 'Muthaiga'),
                  ('Parklands', 'Parklands'),
                  ('Kahawa', 'Kahawa'),
                  ('Kasarani', 'Kasarani'),
                  ('Utawala', 'Utawala')], validators=[DataRequired()])
    propertySize = IntegerField('Property Size (Sqft)', validators=[DataRequired()])
    propertyBedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])
    propertyBathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired()])
    submit = SubmitField('Add ')
