from tkinter import Frame, Label, Button



class Kb_Frame(Frame):
    def __init__(self, master, view):
        super().__init__(master)

        self.view = view

        self.top_row = ['q','w','e','r','t','y','u','i','o','p']
        self.middle_row = ['a','s','d','f','g','h','j','k','l']
        self.bot_rot = ['z','x','c','v','b','n','m']

        self.buttons = []
        self.enter_button = None
        self.delete_button = None

        self.__create_kb()

    def __create_kb(self):

        for i in range(len(self.top_row)):
            self.buttons.append(Button(self, text=self.top_row[i], command=lambda i=self.top_row[i]: self.__button_pressed(i)))
            self.buttons[i].grid(row=0, column=i)

        for i in range(len(self.middle_row)):
            self.buttons.append(Button(self, text=self.middle_row[i], command=lambda i=self.middle_row[i]: self.__button_pressed(i)))
            self.buttons[i + len(self.top_row)].grid(row=1, column=i+1)

        for i in range(len(self.bot_rot)):
            self.buttons.append(Button(self, text=self.bot_rot[i], command=lambda i=self.bot_rot[i]: self.__button_pressed(i)))
            self.buttons[i + len(self.top_row) + len(self.middle_row)].grid(row=2, column=i+1)

        self.enter_button = Button(self, text="Ent", command=self.__enter_pressed)
        self.enter_button.grid(row=1, column=0, rowspan=2, sticky="nsew")

        self.delete_button = Button(self, text="DEL", command=self.__delete_pressed)
        self.delete_button.grid(row=2, column=8, columnspan=2, sticky="nsew")
        
    
    def __button_pressed(self, letter):
        print(letter)

    def __enter_pressed(self):
        self.view.enter_word()

    def __delete_pressed(self):
        self.view.del_word()