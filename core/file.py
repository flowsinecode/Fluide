from tkinter import filedialog

def save_as(get_content):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".flu",
        filetypes=[("Flu files", "*.flu"), ("All files", "*.*")]
    )

    if not file_path:
        return

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(get_content())


def open_file(change_file):
    file_path = filedialog.askopenfilename(
        defaultextension=".flu",
        filetypes=[("Flu files", "*.flu"), ("All files", "*.*")]
    )

    if not file_path:
        return

    with open(file_path, "r", encoding="utf-8") as file:
        change_file(file.read(), file_path)
