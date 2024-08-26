from src.Model.Wordle import Wordle
from src.Model.Word_Generator import Word_Generator
from src.Controller.Word_Guess import Word_Guess

from src.View.View import View


def main():
    wordle = Wordle(buffer_word="closl")
    word_guess = Word_Guess("cllxx")
    wordle.guess(word_guess)

    view = View()

    view.start_mainloop()


if __name__ == "__main__":
    main()
