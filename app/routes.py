from flask import render_template, flash, redirect, url_for, request, Response
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required

from werkzeug.urls import url_parse

from app import myapp_obj
from app.forms import LoginForm, registerForm, TaskForm, ChangeNoteColor, createNote, inviteCollaborator

from app.models import User, Note, Task, collaborators
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

#Merged create_note route with view notes route

# @myapp_obj.route('/create', methods=['POST'])
# @login_required
# def create_note():

#     return render_template('note.html', title='Notes', form = form)

@myapp_obj.route('/notes', methods=['GET', 'POST'])
@login_required
def view_note():
    form = createNote()
    if form.validate_on_submit(): #creates a note once submit button associated with 'form' is pressed, note has backref with current_user
        note = Note(
            author = current_user, body = form.body.data, color = 'Gray'
        )
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('view_note'))

    colorForm = ChangeNoteColor()

    user = current_user
    notes = Note.query.all() 
    final = [] #put all the notes in a list of dictionaries to pass into html function
    for n in notes: 
        shareBool = False
        collaborator = collaborators.query.filter(collaborators.note_id == n.id).all() #search through the collaborators for this note
        for c in collaborator:
            if current_user.username == c.username:
                shareBool = True #is true if the current user is a collaborator for the note
                break

        final.append({'id': n.id, 'timestamp': n.timestamp, 'color': n.color, 'body': n.body, 'user_id' : n.user_id, 'share' : shareBool})



    if colorForm.validate_on_submit():
        id = colorForm.noteID.data
        updateNote = Note.query.filter_by(id = id).first() 

        if updateNote:
            color = colorForm.noteColor.data
            updateNote.color = color
            db.session.commit()
        else:
            flash('Note does not exist')
        return redirect(url_for('view_note'))

    return render_template('notes.html', title='Notes', usernotes=final, colorForm=colorForm, form=form)

@myapp_obj.route('/clearNotes', methods=['GET', 'POST']) 
@login_required
def clear_notes():
        notes = Note.query.all() #gets all notes
        for n in notes:
            if current_user.id == n.user_id: #delete the note only if the current user matches the id of the user who created the note
                db.session.delete(n)
                db.session.commit()
        return redirect(url_for('view_note'))

@myapp_obj.route('/delete/<int:id>', methods=['GET', 'POST']) #gets a note id
@login_required
def delete_note(id):
    delNote = Note.query.filter_by(id=id).first() #find note associated with that note id
    taskQ = Task.query.filter(Task.note_id == id).all() #find all the tasks associated with the note with id <int:id> and delete them
    for n in taskQ: #delete the note after deleting all the tasks
        db.session.delete(n)
    db.session.delete(delNote) 
    db.session.commit()
    return redirect(url_for('view_note'))

@myapp_obj.route('/copy/<int:id>', methods=['GET', 'POST']) #gets note id
@login_required
def copy_note(id):
    copyNote = Note.query.filter_by(id=id).first() #get the note that you want to copy
    note = Note(
        author = current_user, body = copyNote.body, color = copyNote.color #Put all the data of the copy into a new note
    )
    db.session.add(note) #add the new note to database
    db.session.commit()
    return redirect(url_for('view_note'))

#Merged this route with the viewtask route    
# @myapp_obj.route('/task', methods=['GET', 'POST'])
# def createtask():
#     form = TaskForm()

#     if form.validate_on_submit():
#         task = Task(content = form.content.data)
#         db.session.add(task)
#         db.session.commit()
#         flash('Task created')

#     return render_template('task.html', title='Tasks', form=form)

@myapp_obj.route('/deletetask/<int:id>', methods=['GET','POST']) 
@login_required
def deletetask(id): #deletes the first task in a note
    taskQ = Task.query.filter(Task.note_id == id).first() 
    if taskQ is None:
        flash('There is no tasks to delete')
    else:
        db.session.delete(taskQ) 
        db.session.commit()
        flash('Task deleted')

    return redirect(url_for('viewtask', id=id)) 

@myapp_obj.route('/viewtask/<int:id>', methods=['GET','POST']) #gets a note id and views the tasks associated with the note
@login_required
def viewtask(id):
    form = TaskForm()
    note = Note.query.get(id)
    if form.validate_on_submit(): #creates a task once button is clicked, task is associated with the user, current_user and the note with int:id
        task = Task(content = form.content.data, author = current_user, body = note)
        db.session.add(task)
        db.session.commit()
        flash('Task created')

    taskQ = Task.query.filter(Task.note_id == id).all() #find all the tasks associated with the note id
    final = []
    for n in taskQ: #put the tasks into a list of dictionaries
        final.append({'content': n.content , 'id' : n.id})

    return render_template('task.html', title='Tasks', form=form, tasks=final, id=id) #pass the dictionaries into task.html and which note_id the tasks are part of

@myapp_obj.route('/cleartask/<int:id>', methods=['GET','POST']) #gets a note id and clears all tasks associated with that note
@login_required
def clear_tasks(id):
    taskQ = Task.query.filter(Task.note_id == id).all() #find all the tasks associated with the note with the id <int:id>
    for n in taskQ: #delete all notes
        db.session.delete(n)
    db.session.commit()

    return redirect(url_for('viewtask', id=id)) 

@myapp_obj.route('/copytask/<int:id>', methods=['GET','POST']) #gets a task id and copies the id associated with that task
@login_required
def copy_tasks(id):
    taskQ = Task.query.filter(Task.note_id == id).first() #gets the task 
    parentNoteId = taskQ.note_id #gets the id of the parent note
    note = Note.query.get(parentNoteId) #gets the actual parent note so we can backref it (Let the task know that it's associated with that note)
    task = Task(content = taskQ.content, author = current_user, body = note) #create a new task object so we can add it to database

    db.session.add(task)
    db.session.commit()

    return redirect(url_for('viewtask', id=parentNoteId))

@myapp_obj.route('/invite/<int:id>', methods=['GET','POST']) #gets a note id and shares that note to a user
@login_required
def invite(id):
    inviteForm = inviteCollaborator()
    if inviteForm.validate_on_submit():
        note = Note.query.get(id)
        email = inviteForm.collaborator.data
        user = User.query.filter_by(email = email).first()
        if user: 
            collaborator = collaborators(username = user.username, body = note)
            db.session.add(collaborator)
            db.session.commit()
            flash('Successfully invited')
            return redirect(url_for('view_note'))
        else:
            flash('User does not exist')
    return render_template('invite.html', title='Invite', invite = inviteForm)

