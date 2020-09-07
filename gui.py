import functions
import time
from tkinter import messagebox
import tkinter as tk




class Calculator:
    """
    Principal Gui of the program
    """

    def __init__(self):
        self.gui_calcu = tk.Tk()
        self.title = "Visual calculator by INFOLOJO"
        self.gui_calcu.title(self.title)
        self.gui_calcu.geometry("321x435") # el tamaño será de 321 * 435
        self.copyRight()  # Show CopyRight
        self.load_widgets()
        self.gui_calcu.mainloop()



    def copyRight(self):
        """
        show copyRight info about the app
        :return (void):
        """
        messagebox.showinfo("CopyRight","Coded by ajloinformatico.\nI´m open source.\nCopyright © 2020 INFOLOJO")

    def load_widgets(self):
        """
        load widgets
        :return (void):
        """
        pass
