from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class registerForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    username = StringField("Username", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("Sign Up")
    
class TaskForm(FlaskForm):
    content = StringField("Create Task", validators = [DataRequired()])
    submit = SubmitField("Add Task")

class ChangeNoteColor(FlaskForm):
    noteColor = SelectField(
        u'Note color',
        choices = [('White', 'white'), ('LightGray', 'lightgray'), ('CoffeeBrown', 'burlywood'), ('Pink', 'pink'), ('Skyblue', 'skyblue'), 
                   ('Coral', 'coral'), ('Plum', 'plum'), ('LightGreen', 'lightgreen')] )
    noteID = StringField("Note id:", validators = [DataRequired()])
    submit = SubmitField("Change Note Color")

class createNote(FlaskForm):
    body = StringField("Note title:", validators = [DataRequired()])
    submit = SubmitField("Add Note")

class inviteCollaborator(FlaskForm):
    collaborator = StringField("Email of who you want to share note with", validators = [DataRequired()])
    submit = SubmitField("Share")
