
from ui import *

class Fact:
    def __init__(self):
        self.fact = None
        self.answer = None
        self.details = None
    
    def input(self):
        self.fact = uinput(text='Fact:', required=True, example="Leo Tolstoy's year of birth")
        self.answer = uinput(text='Answer:', required=True, example='1828')
        self.details = uinput(text='Pronunciation/mnemonics?', example='tall-stoi')

    def output(self):
        print_accent('\n*** Card ***')
        print(self.fact)
        print_hr()
        print(self.answer)
        if self.details:
            print_hr()
            print(self.details)
        print()

    def save(self, x):
        if self.details:
            m = x.models.byName('Basic+details')
        else:
            m = x.models.byName('Basic')
        x.decks.current()['mid'] = m['id']
        n = x.newNote()
        n['Front'] = self.fact
        n['Back'] = self.answer
        if self.details:
            n['Details'] = self.details
        x.addNote(n)
        x.save()
        print_loud('Card saved!', nl=2)

    @staticmethod
    def anki_note_types():
        return ['Basic', 'Basic+details']
