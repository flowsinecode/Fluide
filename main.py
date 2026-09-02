import customtkinter as ctk
from CTkMenuBarPlus import *
import subprocess
import tkinter.messagebox as messagebox

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

check = subprocess.run(
    ["where","flu"],
    capture_output=True,
    text=True
)

if check.returncode == 0:
    content = ctk.CTkFrame(root)
    content.pack(expand=True, fill="both")

    content.grid_columnconfigure(0, weight=1)
    content.grid_columnconfigure(1, weight=1)
    content.grid_rowconfigure(0, weight=1)

    editor = Editor(content)
    editor.grid(row=0, column=0, sticky="nsew")

    terminal = Terminal(content)
    terminal.grid(row=0, column=1, sticky="nsew")

    compilerpath = check.stdout.strip()

else:
    messagebox.showwarning("Flu Compiler Not found", "Please install it on official Fluentix page.\nFluide will run on Editor-only mode.")
    editor = Editor(root)
    editor.pack(expand=True, fill="both")

    compilerpath = False

file_dropdown = CustomDropdownMenu(file_button)
file_dropdown.add_option(
    option="New"
)
file_dropdown.add_option(
    option="Open"
)
file_dropdown.add_separator()
file_dropdown.add_option(
    option="Save"
)
file_dropdown.add_option(
    option="Save as"
)
file_dropdown.add_separator()

settings_dropdown = file_dropdown.add_submenu("Setting")
settings_dropdown.add_option("Theme")
settings_dropdown.add_option("Editor")
# settings_dropdown.add_option("Compiler")
# settings_dropdown.add_option("AI")
settings_dropdown.add_option("Help")
file_dropdown.add_option(
    option="Exit",
    command=root.destroy
)

edit_dropdown = CustomDropdownMenu(edit_button)
edit_dropdown.add_option(
    option="Undo",
    command=editor.codebox.undo
)
edit_dropdown.add_option(
    option="Redo",
    command=editor.codebox.redo
)
edit_dropdown.add_separator()

edit_dropdown.add_option(
    option="Cut",
    command=editor.codebox.cut_text
)
edit_dropdown.add_option(
    option="Copy",
    command=editor.codebox.copy_text
)
edit_dropdown.add_option(
    option="Paste",
    command=editor.codebox.paste_text
)

edit_dropdown.add_separator()

edit_dropdown.add_option(
    option="Select All",
    command=editor.codebox.select_all_text
)


edit_dropdown.add_separator()

edit_dropdown.add_option(
    option="Search & Replace",
    command=editor.codebox.open_search_window
)

view_dropdown = CustomDropdownMenu(view_button)
view_dropdown.add_option(
    option="Zen mode"
)

root.mainloop()