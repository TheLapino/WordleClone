from src.Controller.Word_Guess import Word_Guess
from src.Model.Word_To_Guess import Word_To_Guess
from src.Model.Letter_Enum import LETTER_STATE


class Word_Evaluator:
    def __init__(self, word_to_guess: Word_To_Guess) -> None:
        self.word_to_guess = word_to_guess
        self.word_length = self.word_to_guess.length()

        self.evaluation = [LETTER_STATE.TBE for i in range(self.word_length)]

        self.word_guess = None
        self.remaining_letter_in_guess = []
        self.remaining_letter_to_guess = []
        self.remaining_letter_in_guess_index = []

    def evaluate_guess(self, word_guess: Word_Guess):
        self.evaluation = [LETTER_STATE.TBE for i in range(self.word_length)]
        self.word_guess = word_guess

        self.__evaluate_good_letter()
        self.__evaluate_wrong_place_letter()
        self.__evaluate_wrong_letter()

        return self.evaluation
        

    def __evaluate_good_letter(self):
        for i in range(self.word_length):
            if self.word_guess.get_word()[i] == self.word_to_guess.get_word()[i]:
                self.evaluation[i] = LETTER_STATE.CORRECT

    def __evaluate_wrong_place_letter(self):
        self.__get_remaining_letters()
        for i in range(len(self.remaining_letter_in_guess)):
            if self.remaining_letter_in_guess[i] in self.remaining_letter_to_guess:
                self.evaluation[self.remaining_letter_in_guess_index[i]] = LETTER_STATE.WRONG_PLACE


    def __evaluate_wrong_letter(self):
        for i in range(self.word_length):
            if self.evaluation[i] == LETTER_STATE.TBE:
                self.evaluation[i] = LETTER_STATE.INCORRECT

    # Fonction un peu laide lmao
    def __get_remaining_letters(self):
        self.remaining_letter_to_guess = []
        self.remaining_letter_in_guess = []
        self.remaining_letter_in_guess_index = []

        for i in range(self.word_length):
            if self.evaluation[i] == LETTER_STATE.TBE:
                self.remaining_letter_to_guess.append(self.word_to_guess.get_word()[i])
                if self.word_guess.get_word()[i] not in self.remaining_letter_in_guess: # on veut pas mettre deux fois la meme lettre en wrong place
                    self.remaining_letter_in_guess.append(self.word_guess.get_word()[i])
                    self.remaining_letter_in_guess_index.append(i) # Garde les indices dans le mot de base pour les référencer

