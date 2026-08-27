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

#Menu bar idk lol

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

file_dropdown = CustomDropdownMenu(file_button)
file_dropdown.add_option(
    option="New",
    accelerator="Ctrl+N"
)
file_dropdown.add_option(
    option="Open",
    accelerator="Ctrl+O"
)
file_dropdown.add_separator()
file_dropdown.add_option(
    option="Save",
    accelerator="Ctrl+S"
)
file_dropdown.add_option(
    option="Save as",
    accelerator="Ctrl+Shift+S"
)
file_dropdown.add_separator()

settings_dropdown = file_dropdown.add_submenu("Setting")
settings_dropdown.add_option("Theme")
# settings_dropdown.add_option("AI")

file_dropdown.add_option(
    option="Exit",
    command=root.destroy,
    accelerator="Alt+F4"
)

edit_dropdown = CustomDropdownMenu(edit_button)
edit_dropdown.add_option(
    option="Undo",
    command=editor.codebox.undo,
    accelerator="Ctrl+Z"
)
edit_dropdown.add_option(
    option="Redo",
    command=editor.codebox.redo,
    accelerator="Ctrl+Y"
)
edit_dropdown.add_separator()

edit_dropdown.add_option(
    option="Cut",
    command=editor.codebox.cut_text,
    accelerator="Ctrl+X"
)
edit_dropdown.add_option(
    option="Copy",
    command=editor.codebox.copy_text,
    accelerator="Ctrl+C"
)
edit_dropdown.add_option(
    option="Paste",
    command=editor.codebox.paste_text,
    accelerator="Ctrl+V"
)




root.mainloop()