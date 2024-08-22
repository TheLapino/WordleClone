from Model.Wordle import Wordle
from Model.Word_Generator import Word_Generator
from src.Controller.Word_Guess import Word_Guess



def main():
    wordle = Wordle(buffer_word="close")
    word_guess = Word_Guess("leave")
    wordle.guess(word_guess)


if __name__ == "__main__":
    main()