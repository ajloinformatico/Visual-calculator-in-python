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
        self.gui_calcu.geometry("341x435")  # el tamaño será de 321 * 435
        self.copyRight()  # Show CopyRight
        self.load_widgets()
        self.gui_calcu.mainloop()

    def copyRight(self):
        """
        show copyRight info about the app
        :return (void):
        """
        messagebox.showinfo("CopyRight", "Coded by ajloinformatico.\nI´m open source.\nCopyright © 2020 INFOLOJO")

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
        pass

    def div_action(self):
        """
        button div
        :return:
        """
        pass

    def seven_action(self):
        """
        button seven
        :return:
        """
        pass

    def eight_action(self):
        """
        button eight
        :return:
        """
        pass

    def nine_action(self):
        """
        button nine
        :return:
        """
        pass

    def por_action(self):
        """
        button nine
        :return:
        """
        pass

    def four_action(self):
        """
        button four
        :return:
        """
        pass

    def five_action(self):
        """
        button five
        :return:
        """
        pass

    def six_action(self):
        """
        button six
        :return:
        """
        pass

    def subtract_action(self):
        """
        button subtract
        """

    def blue_theme_action(self):
        """
        button blue theme
        :return (void) configure widgets with blue style:
        """
        self.result.configure(bg="blue", fg="white", highlightbackground="blue")  # todo insert align right
        self.c.configure(bg="blue", fg="white", highlightbackground="blue")
        self.x_al_cuadrado.configure(bg="blue", fg="white", highlightbackground="blue")
        self.raiz.configure(bg="blue", fg="white", highlightbackground="blue")
        self.div.configure(bg="blue", fg="white", highlightbackground="blue")
        self.seven.configure(bg="blue", fg="white", highlightbackground="blue")
        self.eight.configure(bg="blue", fg="white", highlightbackground="blue")
        self.nine.configure(bg="blue", fg="white", highlightbackground="blue")
        self.por.configure(bg="blue", fg="white", highlightbackground="blue")
        self.four.configure(bg="blue", fg="white", highlightbackground="blue")
        self.five.configure(bg="blue", fg="white", highlightbackground="blue")
        self.six.configure(bg="blue", fg="white", highlightbackground="blue")
        self.subtract.configure(bg="blue", fg="white", highlightbackground="blue")

    def violet_theme_action(self):
        """
        button blue theme
        :return (void) configure widgets with blue style:
        """
        self.result.configure(bg="violet", fg="black", highlightbackground="violet")  # todo insert align right
        self.c.configure(bg="violet", fg="black", highlightbackground="violet")
        self.x_al_cuadrado.configure(bg="violet", fg="black", highlightbackground="violet")
        self.raiz.configure(bg="violet", fg="black", highlightbackground="violet")
        self.div.configure(bg="violet", fg="black", highlightbackground="violet")
        self.seven.configure(bg="violet", fg="black", highlightbackground="violet")
        self.eight.configure(bg="violet", fg="black", highlightbackground="violet")
        self.nine.configure(bg="violet", fg="black", highlightbackground="violet")
        self.por.configure(bg="violet", fg="black", highlightbackground="violet")
        self.four.configure(bg="violet", fg="black", highlightbackground="violet")
        self.five.configure(bg="violet", fg="black", highlightbackground="violet")
        self.six.configure(bg="violet", fg="black", highlightbackground="violet")
        self.subtract.configure(bg="violet", fg="black", highlightbackground="violet")

    def red_theme_action(self):
        """
        button blue theme
        :return (void) configure widgets with blue style:
        """
        self.result.configure(bg="red", fg="black", highlightbackground="red")  # todo insert align right
        self.c.configure(bg="red", fg="black", highlightbackground="red")
        self.x_al_cuadrado.configure(bg="red", fg="black", highlightbackground="red")
        self.raiz.configure(bg="red", fg="black", highlightbackground="red")
        self.div.configure(bg="red", fg="black", highlightbackground="red")
        self.seven.configure(bg="red", fg="black", highlightbackground="red")
        self.eight.configure(bg="red", fg="black", highlightbackground="red")
        self.nine.configure(bg="red", fg="black", highlightbackground="red")
        self.por.configure(bg="red", fg="black", highlightbackground="red")
        self.four.configure(bg="red", fg="black", highlightbackground="red")
        self.five.configure(bg="red", fg="black", highlightbackground="red")
        self.six.configure(bg="red", fg="black", highlightbackground="red")
        self.subtract.configure(bg="red", fg="black", highlightbackground="red")

    def load_widgets(self):
        """
        load widgets
        :return (void):
        todo example
         self.gnuplot_bt = tk.Button(
            self.gui_calcu, text="Plot with Gnuplot", font="Helvetica", command=self.div_action(), highlightbackground="#8EF0F7", pady=2,)
        self.gnuplot_bt.grid(column=0, row=2)
        """
        ####################################### RESULT AREA ###################################################
        self.result = tk.Text(self.gui_calcu, height="2", width="30")
        self.result.configure(background="black", foreground="white")  # todo insert align right
        # self.result.insert(tk.END,"9")
        self.result.grid(column=0, row=0, columnspan=5, pady=(20), padx=(22, 0))
        #######################################  BUTTONS ######################################################

        # ROW 1
        self.c = tk.Button(self.gui_calcu, text="C", width="5", height="2", command=self.c_action)
        self.c.configure(background="black", foreground="white")
        self.c.grid(column=0, row=1, padx=(20, 14))

        self.x_al_cuadrado = tk.Button(self.gui_calcu, text="x²", width="5", height="2",
                                       command=self.x_al_cuadrado_action)
        self.x_al_cuadrado.configure(background="black", foreground="white")
        self.x_al_cuadrado.grid(column=1, row=1, padx=(0, 14))

        self.raiz = tk.Button(self.gui_calcu, text="Raíz", width="5", height="2", command=self.raiz_action)
        self.raiz.configure(background="black", foreground="white")
        self.raiz.grid(column=2, row=1, padx=(0, 14))

        self.div = tk.Button(self.gui_calcu, text="÷", width="5", height="2", command=self.div_action)
        self.div.configure(background="black", foreground="white")
        self.div.grid(column=3, row=1, padx=(0, 14))

        self.blue_theme = tk.Button(self.gui_calcu, text="Blue", width="5", height="2", command=self.blue_theme_action)
        self.blue_theme.configure(background="blue", foreground="white", highlightbackground="blue", relief="ridge")
        self.blue_theme.grid(column=4, row=1)

        # ROW2
        self.seven = tk.Button(self.gui_calcu, text="7", width="5", height="2", command=self.seven_action)
        self.seven.configure(background="black", foreground="white")
        self.seven.grid(column=0, row=2, padx=(20, 14), pady=(20, 0))

        self.eight = tk.Button(self.gui_calcu, text="8", width="5", height="2", command=self.eight_action)
        self.eight.configure(background="black", foreground="white")
        self.eight.grid(column=1, row=2, padx=(0, 14), pady=(20, 0))

        self.nine = tk.Button(self.gui_calcu, text="9", width="5", height="2", command=self.nine_action)
        self.nine.configure(background="black", foreground="white")
        self.nine.grid(column=2, row=2, padx=(0, 14), pady=(20, 0))

        self.por = tk.Button(self.gui_calcu, text="x", width="5", height="2", command=self.por_action)
        self.por.configure(background="black", foreground="white")
        self.por.grid(column=3, row=2, padx=(0, 14), pady=(20, 0))

        self.violet_theme = tk.Button(self.gui_calcu, text="Violet", width="5", height="2",
                                      command=self.violet_theme_action)
        self.violet_theme.configure(background="violet", foreground="black", highlightbackground="violet",
                                    relief="ridge")
        self.violet_theme.grid(column=4, row=2, pady=(20, 0))

        # ROW 3
        self.four = tk.Button(self.gui_calcu, text="4", width="5", height="2", command=self.four_action)
        self.four.configure(background="black", foreground="white")
        self.four.grid(column=0, row=3, padx=(20, 14), pady=(20, 0))

        self.five = tk.Button(self.gui_calcu, text="5", width="5", height="2", command=self.five_action)
        self.five.configure(background="black", foreground="white")
        self.five.grid(column=1, row=3, padx=(0, 14), pady=(20, 0))

        self.six = tk.Button(self.gui_calcu, text="6", width="5", height="2", command=self.six_action)
        self.six.configure(background="black", foreground="white")
        self.six.grid(column=2, row=3, padx=(0, 14), pady=(20, 0))

        self.subtract = tk.Button(self.gui_calcu, text="-", width="5", height="2", command=self.subtract_action)
        self.subtract.configure(background="black", foreground="white")
        self.subtract.grid(column=3, row=3, padx=(0, 14), pady=(20, 0))

        self.red_theme = tk.Button(self.gui_calcu, text="Red", width="5", height="2", command=self.red_theme_action)
        self.red_theme.configure(background="Red", foreground="black", highlightbackground="red", relief="ridge")
        self.red_theme.grid(column=4, row=3, pady=(20, 0))

        # ROW 4

