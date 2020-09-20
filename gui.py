import functions
import time
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


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
        self.fontStyle = tkFont.Font(family="Chalkduster serif", size=20)  # Style for copyright logo on the interface
        ttk.Style().configure('web.TLabel', foreground='blue', background='white')  # Style for web rel
        self.load_widgets()
        self.memory = ""
        self.string_for_result = ""
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
        delete  tk.Text result text
        :return (void):
        """
        self.memory = ""
        self.string_for_result = ""
        self.result.delete("1.0", tk.END)  # 1.0 required to remove

    def seven_action(self):
        """
        button seven
        insert into tk.Text result "7"
        :return (void):
        """
        self.result.insert(tk.END, "7")

    def eight_action(self):
        """
        button eight
        insert into tk.Text result "8"
        :return (void):
        """
        self.result.insert(tk.END, "8")

    def nine_action(self):
        """
        button nine
        insert into tk.Text result "9"
        :return (void):
        """
        self.result.insert(tk.END, "9")

    def four_action(self):
        """
        button four
        insert into tk.Text result "4"
        :return (void):
        """
        self.result.insert(tk.END, "4")

    def five_action(self):
        """
        insert into tk.Text result "5"
        :return (void):
        """
        self.result.insert(tk.END, "5")

    def six_action(self):
        """
        button six
        insert into tk.Text result "6"
        :return (void):
        """
        self.result.insert(tk.END, "6")

    def one_action(self):
        """
        insert into tk.Text result "1"
        :return (void):
        """
        self.result.insert(tk.END, "1")

    def two_action(self):
        """
        button two
        insert into tk.Text result "2"
        :return (void):
        """
        self.result.insert(tk.END, "2")

    def three_action(self):
        """
        button three
        insert into tk.Text result "3"
        :return (void):
        """
        self.result.insert(tk.END, "3")

    ############################################ operations methods #############################################

    def x_al_cuadrado_action(self):
        """
        button x²
        insert into tk.Text result "**"
        :return (void):
        """
        self.result.insert(tk.END, "**")

    def raiz_action(self):
        # todo continue here
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

    def por_action(self):
        """
        button nine
        :return:
        """
        pass

    def subtract_action(self):
        """
        button subtract
        """

    def add_action(self):
        """
        button add
        """

    ######################################### themes methods ###################################################

    def blue_theme_action(self):
        """
        button blue theme
        :return (void) configure widgets with blue style:
        """
        self.result.configure(bg="blue", fg="white", highlightbackground="blue")  # todo insert align right
        self.c.configure(bg="blue", fg="black", highlightbackground="blue")
        self.x_al_cuadrado.configure(bg="blue", fg="black", highlightbackground="blue")
        self.raiz.configure(bg="blue", fg="black", highlightbackground="blue")
        self.div.configure(bg="blue", fg="black", highlightbackground="blue")
        self.seven.configure(bg="blue", fg="black", highlightbackground="blue")
        self.eight.configure(bg="blue", fg="black", highlightbackground="blue")
        self.nine.configure(bg="blue", fg="black", highlightbackground="blue")
        self.por.configure(bg="blue", fg="black", highlightbackground="blue")
        self.four.configure(bg="blue", fg="black", highlightbackground="blue")
        self.five.configure(bg="blue", fg="black", highlightbackground="blue")
        self.six.configure(bg="blue", fg="black", highlightbackground="blue")
        self.subtract.configure(bg="blue", fg="black", highlightbackground="blue")
        self.one.configure(bg="blue", fg="black", highlightbackground="blue")
        self.two.configure(bg="blue", fg="black", highlightbackground="blue")
        self.three.configure(bg="blue", fg="black", highlightbackground="blue")
        self.add.configure(bg="blue", fg="black", highlightbackground="blue")

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
        self.one.configure(bg="violet", fg="black", highlightbackground="violet")
        self.two.configure(bg="violet", fg="black", highlightbackground="violet")
        self.three.configure(bg="violet", fg="black", highlightbackground="violet")
        self.add.configure(bg="violet", fg="black", highlightbackground="violet")

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
        self.one.configure(bg="red", fg="black", highlightbackground="red")
        self.two.configure(bg="red", fg="black", highlightbackground="red")
        self.three.configure(bg="red", fg="black", highlightbackground="red")
        self.add.configure(bg="red", fg="black", highlightbackground="red")

    def cantaloupe_theme_action(self):
        """
        button Cantaloupe theme
        """
        self.result.configure(bg="#78c44b", fg="black", highlightbackground="green")  # todo insert align right
        self.c.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.x_al_cuadrado.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.raiz.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.div.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.seven.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.eight.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.nine.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.por.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.four.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.five.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.six.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.subtract.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.one.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.two.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.three.configure(bg="#78c44b", fg="black", highlightbackground="green")
        self.add.configure(bg="#78c44b", fg="black", highlightbackground="green")

    def original_theme_action(self):
        """
        button original button
        """
        self.result.configure(bg="black", fg="white", highlightbackground="black")  # todo insert align right
        self.c.configure(bg="white", fg="black", highlightbackground="white")
        self.x_al_cuadrado.configure(bg="white", fg="black", highlightbackground="white")
        self.raiz.configure(bg="white", fg="black", highlightbackground="white")
        self.div.configure(bg="white", fg="black", highlightbackground="white")
        self.seven.configure(bg="white", fg="black", highlightbackground="white")
        self.eight.configure(bg="white", fg="black", highlightbackground="white")
        self.nine.configure(bg="white", fg="black", highlightbackground="white")
        self.por.configure(bg="white", fg="black", highlightbackground="white")
        self.four.configure(bg="white", fg="black", highlightbackground="white")
        self.five.configure(bg="white", fg="black", highlightbackground="white")
        self.six.configure(bg="white", fg="black", highlightbackground="white")
        self.subtract.configure(bg="white", fg="black", highlightbackground="white")
        self.one.configure(bg="white", fg="black", highlightbackground="white")
        self.two.configure(bg="white", fg="black", highlightbackground="white")
        self.three.configure(bg="white", fg="black", highlightbackground="white")
        self.add.configure(bg="white", fg="black", highlightbackground="white")

    def random_theme_action(self):
        """
        button random theme
        """
        bg = functions.random_color()
        fg = functions.random_color()
        self.result.configure(bg=bg, fg=fg, highlightbackground=bg)  # todo insert align right
        self.c.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.x_al_cuadrado.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.raiz.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.div.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.seven.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.eight.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.nine.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.por.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.four.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.five.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.six.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.subtract.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.one.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.two.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.three.configure(bg=bg, fg=fg, highlightbackground=bg)
        self.add.configure(bg=bg, fg=fg, highlightbackground=bg)

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
        self.result.configure(bg="black", fg="white", highlightbackground="black")
        self.result.grid(column=0, row=0, columnspan=5, pady=20, padx=(22, 0))
        #######################################  BUTTONS ######################################################

        # ROW 1
        self.c = tk.Button(self.gui_calcu, text="C", width="5", height="2", command=self.c_action)
        self.c.configure(bg="white", fg="black", highlightbackground="white")
        self.c.grid(column=0, row=1, padx=(20, 14))

        self.x_al_cuadrado = tk.Button(self.gui_calcu, text="x²", width="5", height="2",
                                       command=self.x_al_cuadrado_action)
        self.x_al_cuadrado.configure(bg="white", fg="black", highlightbackground="white")
        self.x_al_cuadrado.grid(column=1, row=1, padx=(0, 14))

        self.raiz = tk.Button(self.gui_calcu, text="Raíz", width="5", height="2", command=self.raiz_action)
        self.raiz.configure(bg="white", fg="black", highlightbackground="white")
        self.raiz.grid(column=2, row=1, padx=(0, 14))

        self.div = tk.Button(self.gui_calcu, text="÷", width="5", height="2", command=self.div_action)
        self.div.configure(bg="white", fg="black", highlightbackground="white")
        self.div.grid(column=3, row=1, padx=(0, 14))

        self.blue_theme = tk.Button(self.gui_calcu, text="Blue", width="5", height="2", command=self.blue_theme_action)
        self.blue_theme.configure(background="blue", foreground="black", highlightbackground="blue", relief="ridge")
        self.blue_theme.grid(column=4, row=1)

        # ROW2
        self.seven = tk.Button(self.gui_calcu, text="7", width="5", height="2", command=self.seven_action)
        self.seven.configure(bg="white", fg="black", highlightbackground="white")
        self.seven.grid(column=0, row=2, padx=(20, 14), pady=(20, 0))

        self.eight = tk.Button(self.gui_calcu, text="8", width="5", height="2", command=self.eight_action)
        self.eight.configure(bg="white", fg="black", highlightbackground="white")
        self.eight.grid(column=1, row=2, padx=(0, 14), pady=(20, 0))

        self.nine = tk.Button(self.gui_calcu, text="9", width="5", height="2", command=self.nine_action)
        self.nine.configure(bg="white", fg="black", highlightbackground="white")
        self.nine.grid(column=2, row=2, padx=(0, 14), pady=(20, 0))

        self.por = tk.Button(self.gui_calcu, text="x", width="5", height="2", command=self.por_action)
        self.por.configure(bg="white", fg="black", highlightbackground="white")
        self.por.grid(column=3, row=2, padx=(0, 14), pady=(20, 0))

        self.violet_theme = tk.Button(self.gui_calcu, text="Violet", width="5", height="2",
                                      command=self.violet_theme_action)
        self.violet_theme.configure(background="violet", foreground="black", highlightbackground="violet",
                                    relief="ridge")
        self.violet_theme.grid(column=4, row=2, pady=(20, 0))

        # ROW 3
        self.four = tk.Button(self.gui_calcu, text="4", width="5", height="2", command=self.four_action)
        self.four.configure(bg="white", fg="black", highlightbackground="white")
        self.four.grid(column=0, row=3, padx=(20, 14), pady=(20, 0))

        self.five = tk.Button(self.gui_calcu, text="5", width="5", height="2", command=self.five_action)
        self.five.configure(bg="white", fg="black", highlightbackground="white")
        self.five.grid(column=1, row=3, padx=(0, 14), pady=(20, 0))

        self.six = tk.Button(self.gui_calcu, text="6", width="5", height="2", command=self.six_action)
        self.six.configure(bg="white", fg="black", highlightbackground="white")
        self.six.grid(column=2, row=3, padx=(0, 14), pady=(20, 0))

        self.subtract = tk.Button(self.gui_calcu, text="-", width="5", height="2", command=self.subtract_action)
        self.subtract.configure(bg="white", fg="black", highlightbackground="white")
        self.subtract.grid(column=3, row=3, padx=(0, 14), pady=(20, 0))

        self.red_theme = tk.Button(self.gui_calcu, text="Red", width="5", height="2", command=self.red_theme_action)
        self.red_theme.configure(background="Red", foreground="black", highlightbackground="red", relief="ridge")
        self.red_theme.grid(column=4, row=3, pady=(20, 0))

        # ROW 4
        self.one = tk.Button(self.gui_calcu, text="1", width="5", height="2", command=self.one_action)
        self.one.configure(bg="white", fg="black", highlightbackground="white")
        self.one.grid(column=0, row=4, padx=(20, 14), pady=(20, 0))

        self.two = tk.Button(self.gui_calcu, text="2", width="5", height="2", command=self.two_action)
        self.two.configure(bg="white", fg="black", highlightbackground="white")
        self.two.grid(column=1, row=4, padx=(0, 14), pady=(20, 0))

        self.three = tk.Button(self.gui_calcu, text="3", width="5", height="2", command=self.three_action)
        self.three.configure(bg="white", fg="black", highlightbackground="white")
        self.three.grid(column=2, row=4, padx=(0, 14), pady=(20, 0))

        self.add = tk.Button(self.gui_calcu, text="+", width="5", height="2", command=self.add_action)
        self.add.configure(bg="white", fg="black", highlightbackground="white")
        self.add.grid(column=3, row=4, padx=(0, 14), pady=(20, 0))

        self.cantaloupe_theme = tk.Button(self.gui_calcu, text="Can", width="5", height="2",
                                          command=self.cantaloupe_theme_action)
        self.cantaloupe_theme.configure(background="#78c44b", foreground="black", highlightbackground="green",
                                        relief="ridge")
        self.cantaloupe_theme.grid(column=4, row=4, pady=(20, 0))

        # ROW 5

        self.original_theme = tk.Button(self.gui_calcu, text="original", width="10", height="2",
                                        command=self.original_theme_action)
        self.original_theme.grid(column=0, row=5, columnspan=3, padx=(20, 14), pady=(20, 0))

        self.random_theme = tk.Button(self.gui_calcu, text="random", width="10", height="2",
                                      command=self.random_theme_action)
        self.random_theme.configure(background="pink", foreground="black", relief="ridge")
        self.random_theme.grid(column=2, row=5, columnspan=3, pady=(20, 0))

        # ROW 6
        self.copy = tk.Label(self.gui_calcu, text="Copyright © 2020 INFOLOJO", font=self.fontStyle)
        self.copy.grid(column=0, row=6, columnspan=5, padx=(15, 0), pady=(30, 0))

        # ROW 7
        self.web = ttk.Label(self.gui_calcu, text="https://www.infolojo.es", style='web.TLabel')
        self.web.grid(column=0, row=7, columnspan=5, padx=(15, 0), pady=5)
