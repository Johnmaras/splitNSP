from tkinter import Tk, Button, IntVar, Checkbutton, Label
from tkfilebrowser import askopenfilename as openFile
import os
import splitNSP
file_to_split = None


def on_close():
    root.destroy()


def load_file():
    global file_to_split, messages
    initialDir = os.getcwd()
    filename = openFile(root, initialdir=initialDir, filetypes=[("All types", "*.*")])

    if filename:
        file_to_split = filename
        messages.config(text=f"Loaded file: {file_to_split}")
        return
    messages.config(text=f"File {file_to_split} failed to load!")


def split():
    global quickChkBxVar, messages

    if not file_to_split:
        messages.config(text="Give a file to split")
        return

    varVal = quickChkBxVar.get()
    result = False
    if varVal == 0:
        messages.config(text="Calling copy")
        result = splitNSP.splitCopy(file_to_split)
    elif varVal == 1:
        messages.config(text="Calling quick")
        result = splitNSP.splitQuick(file_to_split)

    messages.config(text=f"The file split was {'successful' if result else 'a failure'}")


root = Tk()
root.protocol("WM_DELETE_WINDOW", on_close)

root.geometry("400x150")

loadBtn = Button(root, text="Load", command=load_file)
loadBtn.pack()

quickChkBxVar = IntVar()
quickChkBx = Checkbutton(root, text="Quick", variable=quickChkBxVar)
quickChkBx.pack()

splitBtn = Button(root, text="Split File", command=split)
splitBtn.pack()

messages = Label(root, text="No messages yet")
messages.pack()

root.mainloop()
