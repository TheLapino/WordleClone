from Controller.Word_Guess import Word_Guess


class Word_Validation:
    def __init__(self, word_length=5, buffer_word="amie"):
        self.word_length = word_length
        self.buffer_word = buffer_word

    def validate_word(self, word_guess: Word_Guess) -> bool:

        words = self.load_words()
        # pas sur que ce check là devrait être ici.
        if word_guess.length() != self.word_length:
            return False

        if word_guess.get_word() not in words:
            return False
        
        return True
    
    def load_words(self):
        return [self.buffer_word]