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


