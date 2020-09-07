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



######################################### LISTENER EVENTS ###################################################

    def c_action(self):
        """
        button c
        :return:
        """
        pass

    def x_al_cuadrado_action(self):
        """
        button x²
        :return:
        """
        pass

    def raiz_action(self):
        """
        button raiz
        :return:
        """

    def div_action(self):
        """
        button div
        :return:
        """

    def blue_theme_action(self):
        """
        button blue theme
        :return (void) configure widgets:
        """
        self.result.configure(background="blue", foreground="white")  # todo insert align right
        self.c.configure(background="blue", foreground="white")
        self.x_al_cuadrado.configure(background="blue", foreground="white")
        self.raiz.configure(background="blue", foreground="white")
        self.div.configure(background="blue", foreground="white")




    def load_widgets(self):
        """
        load widgets
        :return (void):
        """
        ####################################### RESULT AREA ###################################################
        self.result = tk.Text(self.gui_calcu, height="2", width="30")
        self.result.configure(background="black", foreground="white") #todo insert align right
        # self.result.insert(tk.END,"9")
        self.result.grid(column=0, row=0, columnspan=5, pady=(20), padx=(22,0))
        #######################################  BUTTONS ######################################################

        # ROW 1
        self.c = tk.Button(self.gui_calcu, text="C", width="5", height="2", command=self.c_action)
        self.c.configure(background="black", foreground="white")
        self.c.grid(column=0, row=1, padx=(20,14))

        self.x_al_cuadrado = tk.Button(self.gui_calcu, text="x²", width="5", height="2", command=self.x_al_cuadrado_action)
        self.x_al_cuadrado.configure(background="black", foreground="white")
        self.x_al_cuadrado.grid(column=1, row=1, padx=(0,14))


        self.raiz = tk.Button(self.gui_calcu, text="Raíz", width="5", height="2", command=self.raiz_action)
        self.raiz.configure(background="black", foreground="white")
        self.raiz.grid(column=2, row=1, padx=(0,14))

        self.div = tk.Button(self.gui_calcu, text="÷", width="5", height="2", command=self.div_action)
        self.div.configure(background="black", foreground="white")
        self.div.grid(column=3, row=1,padx=(0,14))

        self.blue_theme = tk.Button(self.gui_calcu, text="Blue", width="5", height="2", command=self.blue_theme_action)
        self.blue_theme.configure(background="blue", foreground="white")
        self.blue_theme.grid(column=4, row=1)

        #ROW2


