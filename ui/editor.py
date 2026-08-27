import customtkinter as ctk
from CTkCodeBoxPlus import *

class Editor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.codebox = CTkCodeBox(self, language="python", history_settings=HistorySettings)
        self.codebox.pack(expand=True, fill="both")