**Team-5 Github Repository URL:** https://github.com/Brian1226/TEAM-5

**Team Members Name & Username:** Brian Nguyen (Brian1226), Christy Nguyen (cnguyenth), Karan Sharma (Kar-Sha), Jin You Goh (jackedjin)

**Product Name:** Priority Queue

**Problem Statement:** The to-do app-Priority Queue allows users to collaborate on organizing and prioritzing tasks. The app organize their tasks from greater importance to least importance in a systemic checklist (aka note). After completing a task, the task would be removed and then the next task in queue would take its place. This continues until all tasks are completed. Then, the next checklist (note) in queue will take its place. This continues until all notes are completed.


***


# Use Case Description

**Use Case #1 Name:** Create New Note

**Date:** 4/1/2021


## Summary

Once the user opened the app, they can select the option "Create New Note," which opens up a new empty note.


## Actors

1. The user

## Preconditions

* The user opened the app.


## Triggers

The user clicks on the "Create New Note" option.


## Primary Sequence

1. The user clicks on the "Create New Note" option.
2. The app displays a message, asking the user to either confirm or cancel the action.
3. The user clicks on the "Confirm" option.
4. The app creates a new, empty note.


## Primary Postconditions

* The app creates an empty note.


## Alternate Sequences

3. The user clicks "Cancel" option instead.
    * The app doesn't create a new, empty note.


### Alternate Trigger

* The user clicks on the "Cancel" option.


### Alternate Postconditions

* The app does not create an empty note.


***


**Use Case #2 Name:** Delete Note

**Date:** 4/2/2021


## Summary

To delete a note, the user can select the note, then select the option "Delete Note". 


## Actors

1. The user


## Preconditions

* The selected note has to exist first before a user can delete it.


## Triggers

* The user selects the note they want to delete, then clicks on the "Delete Note" option.


## Primary Sequence

1. The user selects the note they want to delete.
2. The user clicks on the "Delete Note" option.
3. The app displays a message, asking the user to either confirm or cancel the action.
4. The user clicks on the "Confirm" option.
5. The app deletes the selected note.


## Primary Postconditions

* The app deletes the note.


## Alternate Sequences

4. The user clicks on the "Cancel" option instead.
    * The app doesn't delete the selected note.


### Alternate Trigger

* The user clicks on the "Cancel" option.


### Alternate Postconditions

* The note continues to exist.


***


**Use Case #3 Name:** Create New Task

**Date:** 4/3/2021


## Summary

Within the note, a user can create tasks by clicking on the "Create New Task" option.


## Actors

1. The user


## Preconditions

* A note has to exist first before the user can create tasks within it.


## Triggers

* The user clicks on the "Create New Task" option within the note.


## Primary Sequence

1. The user selects a note to go into.
2. The user clicks on the "Create New Task" option.
3. The app displays a message, asking the user to either confirm or cancel the action.
4. The user clicks on the "Confirm" option.
5. The app creates a new task


## Primary Postconditions

* A new line appears within the note, where the user can type in a task.


## Alternate Sequences

4. The user clicks on the "Cancel" option instead.
    * The app doesn't create a new task.


### Alternate Trigger

* The user clicks on the "Cancel" option


### Alternate Postconditions

* No new line for a task appears within the note.


***


**Use Case #4 Name:** Delete Task

**Date:** 4/3/2021


## Summary

The user can select a task within a note, then select the "Delete Task" option to to delete the selected task.


## Actors

1. The user


## Preconditions

* The selected task has to exist within the note first before the user can delete the task.


## Triggers

Within the note, the user selects a task, then clicks on the "Delete Task" option.


## Primary Sequence

1. The user selects a note to go into.
2. The user selects the task they want to delete.
3. The user clicks on the "Delete Task" option.
4. The app displays a message, asking the user to either confirm or cancel the action.
5. The user clicks on the "Confirm" option.
6. The app deletes the selected task.


## Primary Postconditions

* The task gets deleted within the note.


## Alternate Sequences

5. The user clicks on the "Cancel" option instead.
    * The app doesn't delete the selected task


### Alternate Trigger

* The user clicks on the "Cancel" option.


### Alternate Postconditions

* The selected task continues to exist.


***


**Use Case #5 Name:** Make Copy

**Date:** 4/3/2021


## Summary

The user can select a note, and create a copy of it by clicking on the "Make Copy" option. The duplicated note now appears within the app, containing the same tasks.


## Actors
1. The user


## Preconditions

* The selected note must exist first before the user can create a copy of it.


## Triggers

The user selects the note they want to copy, then clicks on the "Make Copy" option.


## Primary Sequence

1. The user selects the note they want to make a copy of.
2. The user clicks on the "Make Copy" option.
3. The app displays a message, asking the user to either confirm or cancel the action.
4. The user clicks on the "Confirm" option.
5. The app creates a copy of the selected note.


## Primary Postconditions

* A copy of the selected note, containing the same tasks, is created.


## Alternate Sequences

4. The user clicks on the "Cancel" option instead.
    * The app doesn't create a copy of the selected note.


### Alternate Trigger

* The user clicks on the "Cancel" option.


### Alternate Postconditions

* A copy of the selected note doesn't get created.


***


**Use Case #6 Name:** Invite Collaborators

**Date:** 4/3/2021


## Summary

The user can invite other people to collaborate, which will give them permission to see, create, and edit each other's notes and tasks.


## Actors

1. The user
2. Invited collaborators


## Preconditions

* The user and the invited collaborators need to be registered.
* The user needs to know the email/username of the people they will invite.


## Triggers

The user clicks on the "Invite Collaborators" option.


## Primary Sequence

1. The user clicks on the "Invite Collaborators" option.
2. The app displays a message, prompting the user for the email of the people to be invited.
3. The user type in the email of the collaborators.
4. The notes and tasks gets shared to the invited collaborators.


## Primary Postconditions

* The user's notes and tasks gets shared to the invited collaborators. Every person can now create, see, and edit each other's notes and tasks.


## Alternate Sequences

3. The user types in an invalid email.
    * The app displays an error message to the user.
    * The app prompts the user to type in a valid email.


### Alternate Trigger

* The user typed an invalid email.


### Alternate Postconditions

* The notes and tasks doesn't get shared. The app displays a error message and prompts the user to type in a valid email.


***


**Use Case #7 Name:** Enable Dark mode

**Date:** 4/3/2021


## Summary

By default, it is black text on a white background. If the user wants a UI where the notes are on a black background with white text instead, they can click on the "Enable Dark Mode" option. Clicking on the option again will revert it back to the original state.


## Actors

1. The user


## Preconditions

* The user opened the app.


## Triggers

The user clicks on the "Enable Dark Mode" option.


## Primary Sequence

1. The user clicks on the "Enable Dark Mode" option.
2. The app's background changes to black and the text's color changes to white.


## Primary Postconditions

* App's background is black, and text's color is white.


## Alternate Sequences

2. The user clicks on the "Enable Dark Mode" option again.
    * Dark mode gets reverted to default state.


### Alternate Trigger

* The user clicks on the "Enabled Dark Mode" option again.


### Alternate Postconditions

* The app is now back to having a white background with black text.


***


**Use Case #8 Name:** Download

**Date:** 4/5/2021


## Summary

This allows users and invited collaborators to download the note. 


## Actors

1. The user


## Preconditions

* The user and the invited collaborators need to be registered.
* The selected note must exist first before the users can download a copy of it.


## Triggers

The users click on the "Download" option.


## Primary Sequence

1. The user navigates and selects the desired note to be downloaded.
2. The user selects the "Download" option.
3. The app displays a message, asking the user to either confirm or cancel the action.
4. The user confirms the "Download" process by selecting the "Confirm" option.
5. The note is downloaded and saved within the user's device. 


## Primary Postconditions

* The note is downloaded into the users' device.


## Alternate Sequences

4. The user selects the "Cancel" option instead.
    * The note doesn't get downloaded. 

### Alternate Trigger

* Upon selecting the "Download" option, the user selects the "Cancel" option. 


### Alternate Postconditions

* The note is not successfully downloaded into the users' device. 


***


**Use Case #9 Name:** Sign up

**Date:** 4/5/2021


## Summary

This allows the user to make an account for the app. 


## Actors

1. The user


## Preconditions

* The user has opened the app.


## Triggers

The user clicks on the "Sign Up" option.


## Primary Sequence

1. The user clicks on the "Sign Up" option.
2. The app prompts the user to enter a username, password, and email.
3. The user provides a username of their account as well as a password.
4. The user provides an email to sign up with.
5. A confirmation email is sent to their email. 



## Primary Postconditions

* The user successfully makes an account.


## Alternate Sequences

3. The user provides an already existing username.
   * The user is unable to successfully make an account.


### Alternate Trigger

* The user's username already exists.


### Alternate Postconditions

* The user is unable to make an account and has to provide a unique username to continue.


***


**Use Case #10 Name:** Log in

**Date:** 4/5/2021


## Summary

This allows the user to be able to log into their account and access their notes. 


## Actors

1. The user


## Preconditions

* The user has to have an account made beforehand.


## Triggers

The user clicks on the "Log In" option.


## Primary Sequence

1. write
2. write


## Primary Postconditions

* write


## Alternate Sequences

write


### Alternate Trigger

* write


### Alternate Postconditions

* write


***

**Use Case #11 Name:** Change Note Color

**Date:** 4/6/2021


## Summary

This allows the user to change the color of an existing note to a different color.


## Actors

1. The user


## Preconditions

* The user already has an existing note.


## Triggers

The user clicks on the "Change Note Color" option within a note.


## Primary Sequence

1. The user selects the note they want to change the color of.
2. The user clicks on the "Change Note Color" option.
3. The app brings up a list of colors.
4. The user clicks on one of the colors.
5. The app displays a message, asking the user to either confirm or cancel the action.
6. The user clicks on the "Confirm" option.
7. The color of the note changes to the user's choice.


## Primary Postconditions

* The chosen note is in a different color.


## Alternate Sequences

6. The user clicks on "Cancel"
   * The note color remains the same.


### Alternate Trigger

* The user clicks on the "Cancel" option.


### Alternate Postconditions

* The color of the note does not change.


***


**Use Case #12 Name:** Change Username/Password

**Date:** 4/6/2021


## Summary

This allows users to change their username or password if forgotten, or for any other reasons.


## Actors

1. The user


## Preconditions

* The user must already have an existing account in order to receive the instructions to change their username/password. 


## Triggers

On the login page, the user selects the option "Forgot Username/Password". 


## Primary Sequence

1. On the login page, the user selects the option "Forgot Username/Password".
2. The user will be prompted to enter account email address to receive further instructions.
3. Upon entering the email address, the user should receive an email with a link, confirming the request for a username/password change. 
4. The link will allow the user to set a new username/password, save the changes, and be directed back to the login page.
5. The user enters the new username/password and logs into the account. 


## Primary Postconditions

* The account's username/password is changed. 


## Alternate Sequences

1. The user logs into the account without selecting the option "Forgot Username/Password".


### Alternate Trigger

* The user does not select the option "Forgot Username/Password".


### Alternate Postconditions

* The user's account username and password remain unchanged. 


***

**Use Case #13 Name:** Set Reminder

**Date:** 4/6/2021

 
## Summary

The user can choose a time and date for a note, which will send the user a notification.

 
## Actors

1. The user


## Preconditions

* A note has to exist first before a user can set a reminder for it.

 
## Triggers

The user clicks on the "Set Reminder" option.

 
## Primary Sequence

1. The user selects a note.
2. The user clicks on the "Set Reminder" option.
3. The app prompts the user for a date and time.
4. The user selects a date and time.
5. The app displays a message, asking the user to either confirm or cancel the action.
6. The user clicks on the "Confirm" option. 
7. The reminder gets set for the note.


## Primary Postconditions

* The reminder gets set for the note, which will send the user a notfication at the chosen time.


## Alternate Sequences

6. The user clicks on the "Cancel" option.
    * A reminder doesn't get set for the note.

 
### Alternate Trigger

* The user clicks on the "Cancel" option.


### Alternate Postconditions

* A reminder doesn't get set for the note. The user will not receive any notification for the note.


***


**Use Case #14 Name:** Add Image

**Date:** 4/6/2021

 
## Summary

The user can add images within a note.

 
## Actors

1. The user


## Preconditions

* A note has to exist before the user can add images within it.

 
## Triggers

The user clicks on the "Add Image" option within the note.

 
## Primary Sequence

1. The user selects a note.
2. The user clicks on the "Add Image" option.
3. The app opens up the user's file manager.
4. The user selects an image.
5. The app displays a message, asking the user to either confirm or cancel the action.
6. The user clicks on the "Confirm" option.
7. The image gets added into the note.


## Primary Postconditions

* The note now contains the selected image.


## Alternate Sequences

6. The user clicks on the "Cancel" option instead.
    * The image doesn't get added into the note.

 
### Alternate Trigger

* The user clicks on the "Cancel" option.


### Alternate Postconditions

* The image doesn't get added into the note.


***


**Use Case #15 Name:** See History

**Date:** 4/6/2021

 
## Summary

A user can see a list of all actions made by other shared users with the date next to them: creation, deletion, and edits of notes and tasks.

 
## Actors

1. The user


## Preconditions

* The user opened the app.

 
## Triggers

The user clicks on the "See History" option.

 
## Primary Sequence

1. The user clicks on the "See History" option.
2. The app displays a list of all actions made by the user and the invite collaborators (if any).


## Primary Postconditions

* A list of all actions made appears.


## Alternate Sequences

None

 
### Alternate Trigger

* None


### Alternate Postconditions

* None


***


## Non-functional Requirements

* A message should be displayed saying that the user added/deleted a note/task successfully.
* Only registered users can share tasks.
* Each note/task should be dated.
* The app displays messages in English.


## Glossary

* user = a person who uses the app
* note = a systematic checklist
* task = each line of the note
* queue = the priority of each note, or the priority of each task within a note


***


## UML Use Case Diagram
![UML](https://cdn1.bbcode0.com/uploads/2021/4/8/d2a563fae6439cb799c3a3845fbd6872-full.png)
