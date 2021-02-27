# Notebook
This program simulates work with notebook

Program can perform these functions:
* Create new note
* Modify existing note
* Show all notes
* Search notes by filter
## Classes
Program consist of these classes:
* Note - represents note with unique id. Also contains text, tags and date
* Notebook - stores and processes information about notes
* Menu - represents interface for working with Notebook
## How to use program
1. Download all files
2. Start Menu.run() from menu.py
3. Choose number of function
## Example of working problem
```
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit

Enter an option: 2
Search for: tasks

1: tasks
2021-02-26
feed the cat

3: tasks
2021-02-27
cleaning

Enter an option: 4
Enter a note id: 1
Enter a memo: feed the dog
Enter tags:

Enter an option: 1

1: tasks
2021-02-26
feed the dog

2: math
2021-02-26
(a+b)^2 = a^2 + 2ab + b^2

3: tasks
2021-02-27
cleaning

Enter an option: 5
Thank you for using your notebook today.
```
