from Controller.Word_Validation import Word_Validation
from Controller.Word_Guess import Word_Guess


class Word_Inputer:
    def __init__(self, word_length=5):
        self.word = []
        self.word_length = word_length
        self.wv = Word_Validation()
        self.assembled_word = ""
        self.is_valid = False

    def add_letter(self, letter):
        if len(self.word) + 1 <= self.word_length:
            self.word.append(letter)
            self.validate_word()

    def remove_letter(self):
        if len(self.word) - 1 >= 0:
            del self.word[-1]
            self.validate_word()

    def validate_word(self):
        self.assemble_word()
        word_guess = Word_Guess(self.assemble_word)
        self.is_valid = self.wv.validate_word(word_guess)

    def assemble_word(self):
        self.assembled_word = ''.join(self.word)

    def get_word_guess(self):
        self.validate_word()

        if self.is_valid():
            return Word_Guess(self.assemble_word)
        
        return None