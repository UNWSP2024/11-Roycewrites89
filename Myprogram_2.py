#Royce Daniel 4/17/2026 "Buttons"

import tkinter
from tkinter import messagebox

class MyGUI:
    def __init__(self):
     self.main_window = tkinter.Tk()
     self.label = tkinter.Label(self.main_window, text="There is info")
     self.my_button = tkinter.Button(self.main_window, text="Show me", command=self.do_something)

     self.quit_button = tkinter.Button(self.main_window, text="No thanks", command=self.main_window.destroy)

     self.quit_button.pack(side = "bottom")
     self.label.pack()
     self.my_button.pack()
     self.main_window.mainloop()


    def do_something(self):
        tkinter.messagebox.showinfo("Here's the info" , "Terrence Fletcher. 214267 Tempo Trail")



if __name__ == "__main__":
    gui = MyGUI()