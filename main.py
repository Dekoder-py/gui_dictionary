import tkinter
from tkinter import ttk

from utils.dictionary import get_definition, get_synonyms


def temp_click():
    print(word.get())


root = tkinter.Tk()

root.title("Dictionary")
root.geometry("1080x720")

definition = ttk.Label(root)

synonyms = ttk.Label(root)

word = tkinter.Variable()

word_input = ttk.Entry(root, textvariable=word)
word_input.grid(row=0, column=0, padx=5, pady=5)

define_button = ttk.Button(
    root, text="Define!", command=lambda: get_definition(definition, word.get())
)
define_button.grid(row=0, column=1, padx=5, pady=5)

synonym_button = ttk.Button(
    root, text="Get Synonyms!", command=lambda: get_synonyms(synonyms, word.get())
)
synonym_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
