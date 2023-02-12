
# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import util
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class Countries():

    def countryFlagImage(self,name):
        image = Image.open('./flags/' + name + '.png')
        image = image.resize((60,40), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        return photo

    def getCountryList(self):
        return self.countryButtonList

    def __init__(self, frame):
        super().__init__()
        COLUMNS = 5
        COUNTRIES = util.get_all_countries()
        self.countryButtonList = [None] * len(COUNTRIES)


        for countryName in COUNTRIES:
            r, c = divmod(COUNTRIES.index(countryName), COLUMNS)
            index = COUNTRIES.index(countryName)
            flag = self.countryFlagImage(countryName)
            
            self.countryButtonList[index] =  SelectedButton(frame, countryName, flag)
            self.countryButtonList[index].get().grid(row=r, column=c)
            self.countryButtonList[index].image = flag # keep a reference!
            # countryButton = SelectedButton(frame, countryName, flag).get()
            # countryButton.grid(row=r, column=c)


class SelectedButton(): 

    selected = False
    bg_selected = "light blue"
    bg_no_selected = "white"
    button = None

    def change(self):
        if self.selected:
            self.button.config(bg=self.bg_no_selected)
        else:
            self.button.config(bg=self.bg_selected)
        self.selected = not self.selected

    def get(self):
        return self.button

    def isSelected(self):
        return self.selected

    def __init__(self, frame, text, image=None):
        self.button = tk.Button(frame, text=text, image=image, bg=self.bg_no_selected, compound='top')
        self.button.config(command=lambda button=self.button: self.change())

class App():

    def __init__(self):
        super().__init__()

        WIDTH = 1100
        HEIGHT = 850

        LEFT_FRAME_WIDTH = (WIDTH/3) * 1
        RIGTH_FRAME_WIDTH = (WIDTH/3) * 2

        OPTIONS = ["building", "car", "dem", "lang", "license", "maps", "phoneme", "skin", "speedcam", "tmc", "userdata"]
        optionButtonList = [None] * len(OPTIONS)


        self = Tk()
        self.title('Igo Primo Update Files')
        self.resizable(1,1)
        self.geometry("{}x{}".format(WIDTH, HEIGHT))
        #self.config(bg="skyblue")


        # Create Left Frame widget
        leftFrame = Frame(self, width=LEFT_FRAME_WIDTH, height=HEIGHT)
        leftFrame.grid(row=0, column=0, padx=10, pady=5)

        # Create destination frame within leftFrame
        destinationFrame = Frame(leftFrame)
        destinationFrame.grid(row=0, column=0, padx=5, pady=5)

        Label(destinationFrame, text="Destination path").grid(row=0, column=0, padx=5, pady=5)
        Label(destinationFrame, text=util.DESTINATION).grid(row=1, column=0, padx=5, pady=5)

        # Create optionsFrame frame within leftFrame
        optionsFrame = Frame(leftFrame)
        optionsFrame.grid(row=1, column=0, padx=5, pady=5)

        # Create label above the tool_bar
        Label(optionsFrame, text="Options").grid(row=0, column=0, padx=5, pady=5)
        # Separator object
        separator = ttk.Separator(optionsFrame, orient='horizontal')
        separator.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        for option in OPTIONS:
            index = OPTIONS.index(option)
            optionButtonList[index] = SelectedButton(optionsFrame, option)
            optionButtonList[index].get().grid(row=index+2, column=0, padx=5, pady=5)

        def copy():
            
            optionsSelected = []
            countriesSelected = []

            # get all options selected
            for option in optionButtonList:
                if option.isSelected():
                    optionsSelected.append(option.get()['text'])

            # get all countries selected
            for country in countries.getCountryList():
                if country.isSelected():
                    countriesSelected.append(country.get()['text'])
            
            print(optionsSelected)
            print(countriesSelected)


        copyButton = Button(leftFrame, text="Copy", command=copy).grid(row=2, column=0, padx=5, pady=5)

        # Create Left Frame widget
        rightFrame = Frame(self, width=RIGTH_FRAME_WIDTH, height=HEIGHT)
        countries = Countries(rightFrame)
        rightFrame.grid(row=0, column=1, padx=10, pady=5)

        self.mainloop()

        
if __name__ == '__main__':
    App()
    