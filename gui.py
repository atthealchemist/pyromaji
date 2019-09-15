import tkinter
import os

from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

from tkinter.scrolledtext import ScrolledText

from engine import TransliterationEngine
from translators import TRANSLATORS


class Gui:

    def __init__(self):

        self.root = tkinter.Tk()
        self.root.iconbitmap(r'{}/assets/pyromaji.ico'.format(os.getcwd()))

        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()

        positionRight = int(
            self.root.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(self.root.winfo_screenheight() /
                           2 - windowHeight / 2)

        self.root.geometry(
            "670x945+{width}+{height}".format(width=positionRight, height=positionDown))
        self.root.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.root.title("PyRomaji GUI")

        labelSource = Label(self.root, text='Source text')
        labelSource.grid(column=0, row=0, padx=4, pady=4, sticky=N + S + E + W)

        self.comboLanguage = Combobox(
            self.root, values=list(TRANSLATORS.keys()), state="readonly")
        self.comboLanguage.grid(
            column=1, row=0, sticky=W + E, padx=4, pady=4,
        )
        self.comboLanguage.current(0)

        buttonLoad = Button(self.root, text="Load", command=self.loadFile)
        buttonLoad.grid(column=2, row=0, padx=4, pady=4, sticky=N + S + E + W)

        self.textBoxSource = ScrolledText(self.root, width=50)
        self.textBoxSource.grid(column=0, columnspan=3,
                                row=1, padx=4, pady=4, sticky=N + S + E + W)

        labelConverted = Label(self.root, text='Converted text')
        labelConverted.grid(column=0, row=3, padx=4,
                            pady=4, sticky=N + S + E + W)

        self.textBoxConverted = ScrolledText(self.root)
        self.textBoxConverted.grid(
            column=0, columnspan=3, row=4, padx=4, pady=4, sticky=N + S + E + W)

        buttonConvert = Button(self.root, text="Convert", command=self.convert)
        buttonConvert.grid(column=0, columnspan=3, row=2, padx=4,
                           pady=4, sticky=N + S + E + W)

        buttonClear = Button(self.root, text="Clear", command=self.clear)
        buttonClear.grid(column=0, row=5, padx=4, pady=4, sticky=N + S + E + W)

        buttonSave = Button(self.root, text="Save to file",
                            command=self.saveFile)
        buttonSave.grid(column=1, row=5, padx=4, pady=4, sticky=N + S + E + W)

        buttonClipboard = Button(
            self.root, text="Copy to clipboard", command=self.copyToClipboard)
        buttonClipboard.grid(column=2, row=5, padx=4,
                             pady=4, sticky=N + S + E + W)

        self.status = Label(self.root, text="",
                            relief=SUNKEN, anchor=W)
        self.status.grid(column=0, columnspan=3, row=6,
                         padx=4, pady=4, sticky=N + S + E + W)

    def log(self, text):
        self.status.config(text=text)

    def clear(self):
        self.textBoxConverted.delete(1.0, END)
        self.textBoxSource.delete(1.0, END)
        self.log("Textboxes were cleared!")

    def convert(self):
        source_text = self.textBoxSource.get("1.0", END)
        language = self.comboLanguage.get()
        engine = TransliterationEngine(translator=TRANSLATORS[language]())
        converted = engine.to_romaji(source_text)

        self.textBoxConverted.delete(1.0, END)
        self.textBoxConverted.insert(END, converted)

        self.log("Successfully converted!")

    def copyToClipboard(self):
        converted = self.textBoxConverted.get("1.0", END)
        self.root.clipboard_append(converted)
        self.log("Copied to clipboard!")

    def closeWindow(self):
        self.root.destroy()

    def loadFile(self):
        text = ''
        filepath = filedialog.askopenfilename(
            initialdir='.',
            title="Select text file",
            filetypes=(("Text documents", "*.txt"), ("All files", "*.*")),
        )
        try:
            with open(filepath, 'r+', encoding="utf-8") as file:
                text = file.read()
                self.textBoxSource.insert(END, text)
                self.log(f"Loaded: {file is not None} @ ({filepath})")
        except Exception as ex:
            self.log(f"Error: {ex}")

    def saveFile(self):
        file = filedialog.asksaveasfile(mode='w', initialdir='.',
                                      title="Save text file as",
                                      defaultextension="*.txt")
        if file is None:
            return
        text = self.textBoxConverted.get(1.0, END)
        file.write(text)
        file.close()
        self.log(f"Saved converted text in file!")



def main():
    sys.argv = ["Main"]

    gui = Gui()
    gui.root.mainloop()


if __name__ == "__main__":
    main()
