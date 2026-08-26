import customtkinter as ctk

class Terminal(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        input_field = ctk.CTkFrame(self)
        input_field.place(relx=0, rely=0, relwidth=1, relheight=0.3)

        input_label = ctk.CTkLabel(input_field, text="Input")
        input_label.pack(fill="x", padx=10, pady=5)

        input_text = ctk.CTkTextbox(input_field)
        input_text.pack(expand=True, fill="both", padx=6, pady=(0, 6))

        output_field = ctk.CTkFrame(self)
        output_field.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

        output_label = ctk.CTkLabel(output_field, text="Output")
        output_label.pack(fill="x", padx=10, pady=5)

        output_text = ctk.CTkTextbox(output_field)
        output_text.configure(state="disabled")
        output_text.pack(expand=True, fill="both", padx=6, pady=(0, 6))