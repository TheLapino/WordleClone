from src.Model.Word_Generator import Word_Generator
from src.Model.Word_Evaluator import Word_Evaluator
from src.Controller.Word_Guess import Word_Guess
from src.Model.Word_To_Guess import Word_To_Guess
from src.Model.Alphabet_Filter import Alphabet_Filter

class Wordle:
    def __init__(self, buffer_word="close"):
        self.af = Alphabet_Filter()
        self.wg = Word_Generator(buffer_word=buffer_word)
        self.word_to_guess = self.wg.get_word(buffer=True)

        self.we = Word_Evaluator(self.word_to_guess)

        self.word_guesses = []
        self.evaluations = []

    def guess(self, word_guess: Word_Guess):
        evaluation = self.we.evaluate_guess(word_guess)
        word_guess.set_evaluation(evaluation)
        self.word_guesses.append(word_guess)
        self.af.filter_guess(word_guess)
        self.af.show_letters()


    def game_loop(self):
        pass