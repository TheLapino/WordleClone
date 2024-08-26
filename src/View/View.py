from src.View.Root import Root
from src.View.Kb_Frame import Kb_Frame
from src.View.Guesses_Frame import Guesses_Frame

class View:
    def __init__(self):
        self.root = Root()

        self.guesses_frame = Guesses_Frame(self.root)
        self.guesses_frame.grid(row=0, column=0, sticky="nsew")

        self.kb_frame = Kb_Frame(self.root, self)
        self.kb_frame.grid(row=1, column=0, sticky="nsew")


    def start_mainloop(self) -> None:
        self.root.mainloop()

    def enter_word(self):
        print("Enter!")

    def del_word(self):
        print("Delete!")