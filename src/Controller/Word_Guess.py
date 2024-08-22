from src.Model.Letter_Enum import LETTER_STATE


class Word_Guess:
    def __init__(self, word):
        self.word = word
        self.evaluation = [LETTER_STATE.TBE for i in range(self.length())]
    
    def get_word(self):
        return self.word
    
    def length(self):
        return len(self.word)
    
    def set_evaluation(self, evaluation):
        self.evaluation = evaluation
    
    def get_evaluation(self):
        return self.evaluation
    

    
