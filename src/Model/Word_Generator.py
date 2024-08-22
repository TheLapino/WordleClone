from src.Model.Word_To_Guess import Word_To_Guess


class Word_Generator:
    def __init__(self, word_length=5, buffer_word="allos"):
        self.word_length = word_length
        self.buffer_word = buffer_word
        

    def get_word(self, buffer=False) -> Word_To_Guess:
        if not buffer:
            word = self.pick_random_word()
            return Word_To_Guess(word)
        return Word_To_Guess(self.buffer_word)
    
    def pick_random_word(self) -> str:
        return "xxxxx"