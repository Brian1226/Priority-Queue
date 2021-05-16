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
    
class NoteForm(FlaskForm):
    content = StringField("Create Note", validators = [DataRequired()])
    submit = SubmitField("Create Note")
    
class TaskForm(FlaskForm):
    content = StringField("Create Task", validators = [DataRequired()])
    submit = SubmitField("Add Task")

class ChangeNoteColor(FlaskForm):
    noteColor = SelectField(
        u'Note color',
        choices = [('White', 'white'), ('Gray', 'gray'), ('Orange', 'orange'), ('Pink', 'pink')] )
    submit = SubmitField("Change Note Color")
    noteID = StringField("Note id:", validators = [DataRequired()])

