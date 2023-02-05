
# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import util
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

WIDTH = 900
HEIGHT = 600

selected_button = None
last_bg = None

class Countries():

    def country(self,name):
        image = Image.open('./flags/' + name + '.png')
        image = image.resize((60,40), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        return photo

    def __init__(self, frame):
        super().__init__()
        COLUMNS = 5
        COUNTRIES = util.get_all_countries() 
        for country_name in COUNTRIES:
            r, c = divmod(COUNTRIES.index(country_name), COLUMNS)
            photo = self.country(country_name)
            label = Label(frame, text=country_name, image=photo, compound='top')
            label.image = photo # keep a reference!
            label.grid(row=r, column=c)

def change_selected_button(button):
    global selected_button, last_bg
    if selected_button is not None:
        selected_button.config(bg=last_bg)
    selected_button = button
    last_bg = button.cget("bg")
    button.config(bg="orange")

def ResponsiveWidget(widget, *args, **kwargs):
    bindings = {'<Enter>': {'state': 'active'},
                '<Leave>': {'state': 'normal'}}

    w = widget(*args, **kwargs)

    for (k, v) in bindings.items():
        w.bind(k, lambda e, kwarg=v: e.widget.config(**kwarg))

    return w

class App():
    def __init__(self):
        super().__init__()

        self = Tk()
        self.title('Igo Primo Update Files')
        self.resizable(1,1)
        self.config(bg="skyblue")

        LEFT_FRAME_WIDTH = (WIDTH/3) * 1
        RIGHT_FRAME_WIDTH = (WIDTH/3) * 2

        # Create Left Frame widget
        left_frame = Frame(self, width=LEFT_FRAME_WIDTH, height=HEIGHT)
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        # Create destination frame within left_frame
        dest_frame = Frame(left_frame,bg="red")
        dest_frame.grid(row=0, column=0, padx=5, pady=5)

        Label(dest_frame, text="Destination path").grid(row=0, column=0, padx=5, pady=5)
        Label(dest_frame, text=util.DESTINATION).grid(row=1, column=0, padx=5, pady=5)

        # Create options_frame frame within left_frame
        options_frame = Frame(left_frame, bg="purple")
        options_frame.grid(row=1, column=0, padx=5, pady=5)

        # Create label above the tool_bar
        Label(options_frame, text="Options").grid(row=0, column=0, padx=5, pady=5)
        # Separator object
        separator = ttk.Separator(options_frame, orient='horizontal')
        separator.grid(row=1, column=0, padx=5, pady=5, sticky="ew")


        button1 = ResponsiveWidget(
            tk.Button,
            options_frame,
            text='abc',
            fg='black',
            activebackground='#B7E3F9',
            activeforeground='black',
            highlightthickness=0,
            relief='flat',
        )

        button1.config(command=lambda button=button1: change_selected_button(button))
        button1.grid(row=2, column=0, padx=5, pady=5)
        #Checkbutton(options_frame, text="building").grid(row=2, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="car").grid(row=3, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="dem").grid(row=4, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="lang").grid(row=5, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="license").grid(row=6, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="maps").grid(row=7, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="phoneme").grid(row=8, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="skin").grid(row=9, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="speedcam").grid(row=10, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="tmc").grid(row=11, column=0, padx=5, pady=5)
        Checkbutton(options_frame, text="userdata").grid(row=12, column=0, padx=5, pady=5)


        button = Button(left_frame, text="Copy").grid(row=2, column=0, padx=5, pady=5)

        



        # Create Left Frame widget
        right_frame = Frame(self, width=RIGHT_FRAME_WIDTH, height=HEIGHT)
        countries = Countries(right_frame)
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        self.mainloop()

        
if __name__ == '__main__':
    App()
    