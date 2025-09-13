import tkinter
from tkinter import ttk

from utils.dictionary import get_definition


def temp_click():
    print(word.get())


root = tkinter.Tk()

root.title("Dictionary")
root.geometry("1080x720")

word = tkinter.Variable()
word_input = ttk.Entry(root, textvariable=word)

word_input.pack()
define_button = ttk.Button(
    root, text="Define!", command=lambda: get_definition(word.get())
)  # TODO: Make this button call definition
define_button.pack()

root.mainloop()
