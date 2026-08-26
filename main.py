import customtkinter as ctk
from CTkMenuBarPlus import *

from ui.editor import Editor
from ui.terminal import Terminal
from ui.action import Action

root = ctk.CTk()
root.title("Fluide")
root.geometry('1200x750')

menu_bar = CTkMenuBar(root)
file_button = menu_bar.add_cascade("File")
edit_button = menu_bar.add_cascade("Edit")
view_button = menu_bar.add_cascade("View")
go_button = menu_bar.add_cascade("Go")

action = Action(root)
action.pack(fill="x", padx=8, pady=8)

content = ctk.CTkFrame(root)
content.pack(expand=True, fill="both")

content.grid_columnconfigure(0, weight=1)
content.grid_columnconfigure(1, weight=1)
content.grid_rowconfigure(0, weight=1)

editor = Editor(content)
editor.grid(row=0, column=0, sticky="nsew")

terminal = Terminal(content)
terminal.grid(row=0, column=1, sticky="nsew")


root.mainloop()