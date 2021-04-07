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

The user clicks on the "Create New Note" option, and then clicks on the "Confirm" option.


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

* The user selects the note they want to delete, clicks on the "Delete Note" option, then clicks on the "Confirm" option.


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

* The app does not delete the note.


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

* The user clicks on the "Create New Task" option within the note, and clicks on the "Confirm" option


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

Within the note, the user selects a task, clicks on the "Delete Task" option, then clicks on the "Confirm" option.


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

* The selected task doesn't get deleted.


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

The user selects the note they want to copy, clicks on the "Make Copy" option, then clicks on the "Confirm" option.


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


## Preconditions

* The user and the invited collaborators need to be registered.
* The user needs to know the email/username of the people they will invite.


## Triggers

The user clicks on the "Invite Collaborators" option.


## Primary Sequence

1. The user clicks on the "Invite Collaborators" option.
2. The app displays a message, prompting the user for the email of the people to be invited.
3. The user type in the email of the collaborators.


## Primary Postconditions

* The user's notes and tasks gets shared to the invited collaborators. Every person can now create, see, and edit each other's notes and tasks.


## Alternate Sequences

3. The user types in an invalid email.
    * The app displays an error message to the user.
    * The app prompts the user to type in a valid email.


### Alternate Trigger

* The user types in the collaborator's email again.


### Alternate Postconditions

* The app will continue displaying the error message and prompting for valid email, until the user types a valid email.


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
2. The app's background changes to black and the text's color changes to white, if the user don't click on the option again.


## Primary Postconditions

* App's background is black, and text's color is white.


## Alternate Sequences

2. The user clicks on the "Enable Dark Mode" option again instead.
    * Dark mode gets reverted to default state.


### Alternate Trigger

* The user clicks on the "Enabled Dark Mode" option again.


### Alternate Postconditions

* the app is now back to having a white background with black text.


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

4. The user selects the "Cancel" option instead
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
2. The user provides a username of their account as well as a password.
3. The user provides an email to sign up with.
4. A confirmation email is sent to their email. 



## Primary Postconditions

* The user successfully makes an account.


## Alternate Sequences

2. The user provides an already existing username
   * The user is unable to successfully make an account.


### Alternate Trigger

* The user's username already exists


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

1. The user clicks on the note they want to change the color of.
2. The user clicks on the "Change Note Color" option.
3. The app brings up a list of colors.
4. The user clicks on one of the colors.
5. The color of the note changes to the user's choice.


## Primary Postconditions

* The chosen note is in a different color.


## Alternate Sequences

3. The user clicks on "Cancel"
   * The note color remains the same.


### Alternate Trigger

* The user clicks on the "Cancel" option.


### Alternate Postconditions

* The color of the note does not change.


***


**Use Case #12 Name:** 

**Date:** 4/6/2021


## Summary

write


## Actors

1. The user


## Preconditions

* write


## Triggers

write


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


## Primary Postconditions

* The reminder gets set for the note.


## Alternate Sequences

3. The user clicks on the "Cancel" option.
    * A reminder doesn't get set for the note.

 
### Alternate Trigger

* The user clicks on the "Cancel" option.


### Alternate Postconditions

* A reminder doesn't get set for the note. The user will not receive any notification for the note.


***


## Non-functional Requirements

* A message should be displayed saying that the user added/deleted a note/task successfully
* Only registered users can share tasks
* Each note/task should be dated


## Glossary

* user = a person who uses the app
* note = a systematic checklist
* task = each line of the note
* queue = the priority of each note, or the priority of each task within a note

