"""Simple Caluclator Program"""

from tkinter import *  # Importing Everthing from Tkinter

__author__ = "Kartikey"
__version__ = "1.0.0"
__maintainer__ = "Kartikey"
__email__ = "kryptyls@gmail.com"
__date__ = "17.8.2021"


def getResult(event=None):
    """Gives the result of the equation written in Calculation Bar"""
    # Replace Characters in the equation
    equation = calculationBar.get().replace(
        '^', '**').replace('\u00d7', '*').replace('\u00f7', '/')
    try:
        equation = eval(equation)
    except:
        equation = 'Error!'
    calculationBar.delete(0, END)
    calculationBar.insert(END, equation)


def remindResult():
    """Consotantly update the result of Equation written in Calculation Bar"""
    equation = calculationBar.get().replace(
        '^', '**').replace('\u00d7', '*').replace('\u00f7', '/')
    try:
        equation = eval(equation)
    except:
        equation = 'Error!'
    # Updating the Result
    calculationResultBar.delete(0, END)
    calculationResultBar.insert(END, equation)
    # Changing The Focus to Calculation Bar if focus is changed
    calculationBar.focus()
    calculationResultBar.xview_moveto(1)
    root.after(1, remindResult)


def keyPressed(event):
    """Assigning actions to SOme Certain Keys"""
    # TODO: Add action when a key other than these are pressed.
    charPressed = str(event.char)
    if charPressed in operatorsAndNumbers:
        pass
    elif charPressed == 'c' or charPressed == 'C':
        calculationBar.delete(0, END)
    elif charPressed == ' ':
        pos = calculationBar.index(INSERT)
        calculationBar.delete(pos-1, pos)
    elif charPressed == '=':
        pos = calculationBar.index(INSERT)
        calculationBar.delete(pos-1, pos)
        getResult()


class calculatorButton():
    """Styled Button for this Calculator
    -> the button will change colour if mouse pointer
    -> is above the button."""

    def __init__(self, master=NONE, text='0', command=None, bg='#10111b', fg='white', relief=FLAT, font='consolas 23 bold', bd=0, side=LEFT, expand=YES, fill=BOTH, anchor=CENTER):
        if command == None:
            command = self.enterNumber
        self.button = Button(master, text=text, font=font,
                             relief=relief, bg=bg, fg=fg, command=command, bd=bd)
        self.button.pack(side=side, anchor=anchor, expand=expand, fill=fill)
        self.button.bind('<Enter>', self.focusButton)
        self.button.bind('<Leave>', self.focusButton)

    def focusButton(self, event=None):
        """Changes Colour if mouse pointers hover above the button"""
        event = str(event)[1:6]
        if event == 'Enter':
            self.button.config(bg='grey')
        else:
            self.button.config(bg='#10111b')

    def enterNumber(self):
        """Insert character when button is clicked"""
        number = self.button['text']
        if number == '=':
            getResult()
        elif number == 'C':
            calculationBar.delete(0, END)
        elif number == ' \u232b ':
            pos = calculationBar.index(INSERT)
            calculationBar.delete(pos-1, pos)
        else:
            posCursor = calculationBar.index(INSERT)
            calculationBar.insert(posCursor, number)


if __name__ == '__main__':

    # Defining Window
    root = Tk()
    root.geometry('400x400+250+250')
    root.resizable(False, False)  # Non Resizable Window
    root.title('Sky Dive Calculator')
    root.config(bg='#10111b')

    # Keys that can be pressed
    operatorsAndNumbers = list(
        map(str, ['+', '-', '*', '/', '^', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '.']))

    # Defining Frames
    calculationFrame, buttonsFrame = Frame(bg='yellow'), Frame(bg='red')
    calculationFrame.pack(fill=BOTH)
    buttonsFrame.pack(fill=BOTH, expand=YES)

    # Items in Calculation Frame
    # Main Entry Widget
    calculationBar = Entry(calculationFrame, font='consolas 30', justify=RIGHT, bg='#10111b',
                           fg='white', bd=0, cursor='xterm', insertbackground='#53acb0', insertwidth=3)
    # Secondary Entry Widget
    # -> shows the result constantly
    calculationResultBar = Entry(calculationFrame, font='consolas 15',
                                 justify=RIGHT, bg='#10111b', fg='white', text='0', bd=0)
    calculationBar.pack(fill=BOTH, expand=YES)
    calculationResultBar.pack(fill=BOTH, expand=YES, side=LEFT)
    calculatorButton(calculationFrame, text=' \u232b ',
                     expand=NO, font='consolas 19')

    # Items in Buttons Frame
    # Definign Layers for Buttons
    layer1, layer2, layer3, layer4, layer5 = Frame(buttonsFrame), Frame(
        buttonsFrame), Frame(buttonsFrame), Frame(buttonsFrame), Frame(buttonsFrame)
    layer1.pack(fill=BOTH, expand=YES,), layer2.pack(fill=BOTH, expand=YES), layer3.pack(
        fill=BOTH, expand=YES), layer4.pack(fill=BOTH, expand=YES), layer5.pack(fill=BOTH, expand=YES)

    # Organizing Everything In Lists
    layers = [layer1, layer2, layer3, layer4, layer5]
    layersText = [['C', '(', ')', '\u00f7'],
                  ['7', '8', '9', '\u00d7'],
                  ['4', '5', '6', '-'],
                  ['1', '2', '3', '+'],
                  ['^', '0', '.', '=']]

    # Defining Buttons for this calculator
    n = 0
    for i in layersText:
        for j in range(4):
            calculatorButton(layers[n], text=i[j])
        n += 1

    # Foucs on the Calulation Bar
    calculationBar.focus()

    # updating the result
    remindResult()

    # Binding Keys
    root.bind('<KeyPress>', keyPressed)
    root.bind('<Return>', getResult)
    root.bind('<Tab>', NONE)

    # Looping the Window
    root.mainloop()
