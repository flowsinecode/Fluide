import customtkinter as ctk
from CTkCodeBoxPlus import *

class Editor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        codebox = CTkCodeBox(self, language="python")
        codebox.pack(expand=True, fill="both")