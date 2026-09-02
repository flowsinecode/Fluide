import customtkinter as ctk
from CTkCodeBoxPlus import *

class Editor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.codebox = CTkCodeBox(self, language="python")
        self.codebox.pack(expand=True, fill="both")
        self.codebox.set_history_enabled("enabled")

    def get_content(self):
        return self.codebox.get("1.0", "end")