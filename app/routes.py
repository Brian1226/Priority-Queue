from flask import render_template, flash, redirect
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required

from app import myapp_obj
from app.forms import LoginForm, registerForm

from app.models import User
from app import db

@myapp_obj.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data): # redirect back to login page if invalid user / password
            flash('Invalid username or password')
            return redirect('/')

    # WORK IN PROGRESS

    return render_template('login.html', title='Sign In', form=form)



@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()

    if form.validate_on_submit(): 
        user = User.query.filter_by(username = form.username.data).first()
        email = User.query.filter_by(email = form.email.data).first()
        if user:
            print(f'Username is already taken') #should be a flash message
        elif email:
            print(f'Email is already taken') #should be a flash message
        else:
            user = User(username = form.username.data, email = form.email.data, password = form.password.data)
            db.session.add(user)
            db.session.commit()
            print(f'Registered user {user.username}') #for testing purposes, remove this later

    return render_template('registerpage.html', form=form)
