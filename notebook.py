'''This module works with notes and notebook'''
import datetime
# Store the next available id for all new notes
LAST_ID = 0

class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''

    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global LAST_ID
        LAST_ID += 1
        self.note_id = LAST_ID

    def match(self, searched_text):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags.'''
        return searched_text in self.memo or searched_text in self.tags


class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))

    def find_note(self, note_id):
        '''Find and return note by id if it exist'''
        for note in self.notes:
            if str(note.note_id) == note_id:
                return note
        print("Note with this id doesn't exist")
        return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self.find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        tags to the given value.'''
        note = self.find_note(note_id)
        if note:
            note.tags = tags

    def search(self, searched_text):
        '''Find all notes that match the given filter
        string.'''
        return [note for note in self.notes if note.match(searched_text)]
