'''This module is interface for working with class Notebook'''
import sys
from notebook import Notebook

class Menu:
    '''Display a menu and respond to choices when run.'''

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_note,
        "4": self.modify_note,
        "5": self.quit
        }

    def display_menu(self):
        '''Show menu with variants of function'''
        print("""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        '''Show all notes (id, tags, date, text)'''
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"\n{note.note_id}: {note.tags}\n{note.creation_date}\n{note.memo}")

    def search_notes(self):
        '''Show notes that contain inputed text'''
        searched_text = input("Search for: ")
        notes = self.notebook.search(searched_text)
        self.show_notes(notes)

    def add_note(self):
        '''Create new note'''
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")

    def modify_note(self):
        '''Modify existing note'''
        note_id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            if not self.notebook.modify_memo(note_id, memo):
                return
        if tags:
            self.notebook.modify_tags(note_id, tags)


    def quit(self):
        '''Ends the program'''
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
