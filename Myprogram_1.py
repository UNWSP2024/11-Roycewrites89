#Royce Daniel 4/17/2026 "Wise Window"
import tkinter


class box:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Optimus Prime')
        self.label = tkinter.Label(self.main_window, text="'Every sentient being has the capacity for change.'")
        self.label.pack(side = tkinter.TOP)
        self.main_window.mainloop()

if __name__ == "__main__":
    MyGUI=box()

