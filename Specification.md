**Team-5 Github Repository URL:** https://github.com/Brian1226/TEAM-5

**Team Members Name & Username:** Brian Nguyen (Brian1226), Christy Nguyen (cnguyenth), Karan Sharma (Kar-Sha)

**Product Name:** Priority Queue

**Problem Statement:** The to-do app-Priority Queue allows users to collaborate on organizing and prioritzing tasks. The app organize their tasks from greater importance to least importance in a systemic checklist (aka note). After completing a task, the task would be removed and then the next task in queue would take its place. This continues until all tasks are completed. Then, the next checklist (note) in queue will take its place. This continues until all notes are completed.


***


# Use Case Description

**Use Case #1 Name:** Create new note

**Date:** 4/1/2021

 
## Summary

Once the user opened the app, they can select the option "Create new note," which opens up a new empty note.

 
## Actors

1. The user


## Preconditions

* The user opened the app.

 
## Triggers

The user clicks on the "Create new note" option, and then clicks on the "Confirm" option.

 
## Primary Sequence

1. The user clicks on the "Create new note" option.
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


**Use Case #2 Name:** Delete note

**Date:** 4/2/2021

 
## Summary

To delete a note, the user can select the note, then select the option "delete note". 

 
## Actors

1. The user


## Preconditions

* The selected note has to exist first before a user can delete it.

 
## Triggers

* The user selects the note they want to delete, clicks on the "Delete note" option, then clicks on the "Confirm" option.

 
## Primary Sequence

1. The user selects the note they want to delete.
2. The user clicks on the "Delete note" option.
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


**Use Case #3 Name:** Create new task

**Date:** 4/3/2021

 
## Summary

Within the note, a user can create tasks by clicking on the "Create new task" option.

 
## Actors

1. The user


## Preconditions

* A note has to exist first before the user can create tasks within it.

 
## Triggers

* The user clicks on the "Create new task" option within the note, and clicks on the "Confirm" option

 
## Primary Sequence

1. The user selects a note to go into.
2. The user clicks on the "Create new task" option.
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


**Use Case #4 Name:** Delete task

**Date:** 4/3/2021

 
## Summary

The user can select a task within a note, then select the "Delete task" option to to delete the selected task.

 
## Actors

1. The user


## Preconditions

* The selected task has to exist within the note first before the user can delete the task.

 
## Triggers

Within the note, the user selects a task, clicks on the "Delete task" option, then clicks on the "Confirm" option.

 
## Primary Sequence

1. The user selects a note to go into.
2. The user selects the task they want to delete.
3. The user clicks on the "Delete task" option.
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


**Use Case #5 Name:** Make copy

**Date:** 4/3/2021

 
## Summary

The user can select a note, and create a copy of it by clicking on the "Make copy" option. The duplicated note now appears within the app, containing the same tasks.

 
## Actors
1. The user


## Preconditions

* The selected note must exist first before the user can create a copy of it.

 
## Triggers

The user selects the note they want to copy, clicks on the "Make copy" option, then clicks on the "Confirm" option.

 
## Primary Sequence

1. The user selects the note they want to make a copy of.
2. The user clicks on the "Make copy" option.
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


## Non-functional Requirements

*
*
*

 
## Glossary

* user = a person who uses the app
* note = a systematic checklist
* task = each line of the note
* queue = the priority of each list, or the priority of each tasks within a list (the elements are in order from most important to least, from top to bottom)
