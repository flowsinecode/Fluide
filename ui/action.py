import customtkinter as ctk
from CTkCodeBoxPlus import *

from core import run

class Action(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.name_file = ctk.CTkLabel(self, text="Untitled")
        self.name_file.pack(side="left", padx=10, pady=5)

        run_button = ctk.CTkButton(self, text="▶ Run", width=84, height=34, corner_radius=6, command=run.run)
        run_button.pack(side="right", padx=10, pady=5)