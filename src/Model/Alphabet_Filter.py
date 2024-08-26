import string

from src.Model.Letter_Enum import LETTER_STATE
from src.Controller.Word_Guess import Word_Guess

class Alphabet_Filter:
    def __init__(self) -> None:
        
        self.correct_letter = set()
        self.incorrect_letter = set()
        self.wrong_place_letter = set()
        self.tbe_letter = set(string.ascii_lowercase)
    
    def filter_guess(self, word_guess: Word_Guess):
        self.correct_letter.update(self.filter_letter(word_guess, LETTER_STATE.CORRECT))
        self.incorrect_letter.update( self.filter_letter(word_guess, LETTER_STATE.INCORRECT))
        self.wrong_place_letter.update(self.filter_letter(word_guess, LETTER_STATE.WRONG_PLACE))
        self.tbe_letter = self.tbe_letter - self.correct_letter - self.incorrect_letter - self.wrong_place_letter

    def filter_letter(self, word_guess: Word_Guess, letter_state):
        filtered_letters = []
        for i, evaluation in enumerate(word_guess.get_evaluation()):
            if evaluation == letter_state:
                filtered_letters.append(word_guess.get_word()[i])
        return filtered_letters
    
    def show_letters(self):
        print(f"correct {len(self.correct_letter)}: {self.correct_letter}")
        print(f"incorrect {len(self.incorrect_letter)}: {self.incorrect_letter}")
        print(f"wrong place {len(self.wrong_place_letter)}: {self.wrong_place_letter}")
        print(f"TBE {len(self.tbe_letter)}: {self.tbe_letter}")