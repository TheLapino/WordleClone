class Word_To_Guess:
    def __init__(self, word):
        self.word = word
        self.dupes = []
        self.__detect_duplicate()

    def __detect_duplicate(self):
        seen = set()
        self.dupes = [x for x in self.word if x in seen or seen.add(x)]

    def length(self):
        return len(self.word)

    def __str__(self) -> str:
        return self.word
    
    def get_word(self):
        return self.word
    
    def get_dupes(self):
        return self.dupes