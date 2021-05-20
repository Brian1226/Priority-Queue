from flask import render_template, flash, redirect, url_for, request, Response
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required

from werkzeug.urls import url_parse

from app import myapp_obj
from app.forms import LoginForm, registerForm, NoteForm, TaskForm, ChangeNoteColor

from app.models import User, Note, Task
from app import db
from datetime import datetime

@myapp_obj.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('view_note'))

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None:
            flash('Username does not exist')
            return redirect('/')

        elif not user.check_password(form.password.data):
            flash('Incorrect password')
            return redirect('/')

        else:
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('view_note')
            return redirect(next_page)

    return render_template('login.html', title='Log In', form=form)



@myapp_obj.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        email = User.query.filter_by(email = form.email.data).first()

        if user:
            flash('Username is already taken')
            return redirect(url_for('register'))

        elif email:
            flash('Email is already taken')
            return redirect(url_for('register'))

        else:
            user = User(username = form.username.data, email = form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Successfully registered')
            return redirect(url_for('login'))

    return render_template('registerpage.html', title='Register', form=form)

@myapp_obj.route('/create_note', methods=['GET', 'POST'])
@login_required
def create_note():
    noteForm = NoteForm()
    if noteForm.validate_on_submit():
        if len(noteForm.content.data) > 0:
            note = Note(
                author = current_user, body = noteForm.content.data, color = 'White'
            )
            db.session.add(note)
            db.session.commit()
            flash('Note created')
            return redirect(url_for('view_note'))
    return render_template('note.html', title='Notes', noteForm = noteForm)

@myapp_obj.route('/notes', methods=['GET', 'POST'])
@login_required
def view_note():
    colorForm = ChangeNoteColor()
    user = current_user
    notes = user.notes.all()
    final = []
    for n in notes:
        information = []
        information.append(n.body)
        information.append(n.timestamp)
        final.append(information)

    color = 'White'
    if colorForm.validate_on_submit():
        id = colorForm.noteID.data
        updateNote = Note.query.filter_by(id = id).first() 
        color = colorForm.noteColor.data

        if updateNote:
            updateNote.color = color
            db.session.commit()
        else:
            flash('Note does not exist')
        return redirect(url_for('view_note')) #color of paragraph in html will change back upon refreshing since the color isn't stored in the database

    return render_template('notes.html', title='Notes', usernotes=final, colorForm=colorForm, color=color)


@myapp_obj.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_note(id):
    delNote = Note.query.filter_by(id=id).first() 
    taskQ = Task.query.filter(Task.note_id == id).all() 
    for n in taskQ: 
        db.session.delete(n)
    db.session.delete(delNote) 
    db.session.commit()
    return redirect(url_for('view_note'))

@myapp_obj.route('/clearnotes', methods=['GET', 'POST'])
@login_required
def clear_notes():
    notes = Note.query.all() 
    for n in notes:
        if current_user.id == n.user_id: 
            db.session.delete(n)
            db.session.commit()
    return redirect(url_for('view_note'))
    
@myapp_obj.route('/task', methods=['GET', 'POST'])
@login_required
def task():
    taskForm = TaskForm()
    #note = Note.query.get(id)
    if taskForm.validate_on_submit():
        task = Task(content = taskForm.content.data, author = current_user)
        db.session.add(task)
        db.session.commit()
        flash('Task created')

    allTask = Task.query.all() #find all the tasks associated with the note id
    final = []
    for n in allTask: #put the tasks into a list of dictionaries
        final.append({'content': n.content, 'user_id':n.user_id})

    return render_template('task.html', title='Tasks', form=taskForm, tasks=final)

@myapp_obj.route('/deletetask', methods=['GET','POST']) 
@login_required
def deletetask():
    taskForm = TaskForm()
    #taskQ = Task.query.filter(Task.note_id == id).first() #this one should get the note id from the url, maybe, i didn't test it
    delTask = Task.query.filter(Task.user_id == current_user.id).first()
    if delTask is None:
        flash('There are no tasks to delete!')
    else:
        db.session.delete(delTask)
        db.session.commit()
        flash('Task deleted')

    return redirect(url_for('task')) #should really return a redirect to /viewtask/<int:id> but I couldn't get it to work

@myapp_obj.route('/cleartask', methods=['GET','POST']) #gets a note id and clears all tasks associated with that note
@login_required
def cleartask():
    allTask = Task.query.filter(Task.user_id == current_user.id).all() #find all the tasks associated with the note with the id <int:id>
    for n in allTask: #delete all notes
        db.session.delete(n)
        db.session.commit()

    return redirect(url_for('task'))

@myapp_obj.route('/copytask', methods=['GET','POST']) #gets a task id and copies the id associated with that task
@login_required
def copytask():
    task = Task.query.filter(Task.user_id == current_user.id).first() #gets the task 
    parentUserId = task.user_id #gets the id of the parent note
    #note = Note.query.get(parentNoteId) #gets the actual parent note so we can backref it (Let the task know that it's associated with that note)
    tasks = Task(content = task.content, author = current_user) #create a new task object so we can add it to database

    db.session.add(tasks)
    db.session.commit()

    return redirect(url_for('task')) 
