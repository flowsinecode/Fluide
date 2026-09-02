from tkinter import filedialog
from ui.editor import Editor

def save_as():
    file = filedialog.asksaveasfile()
    with open(file, "w", "utf-8") as f:
        f.write(Editor.get_content)

        #! Bug here


def open():
    filedialog.askopenfile()