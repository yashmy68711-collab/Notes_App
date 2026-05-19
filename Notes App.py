import tkinter as tk
from tkinter import messagebox

def save_notes():
    text = note_area.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showerror(
            "Error",
            "Note cannot be empty"
        )
        return

    with open("notes.txt", "a") as file:
        file.write(text + "\n")
        file.write("-" * 30 + "\n")

    messagebox.showinfo(
        "Saved",
        "Notes saved successfully!"
    )

def clear_notes():
    note_area.delete("1.0", tk.END)

window = tk.Tk()
window.title("Simple Notes App")
window.geometry("500x400")

title = tk.Label(
    window,
    text="Notes App",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)

note_area = tk.Text(
    window,
    width=50,
    height=15,
    font=("Arial", 12)
)

note_area.pack(pady=10)

save_btn = tk.Button(
    window,
    text="Save Notes",
    command=save_notes,
    width=20
)

open_btn = tk.Button(
    window,
    text="Open Notes",
    command=open_notes,
    width=20
)


save_btn.pack(pady=5)

clear_btn = tk.Button(
    window,
    text="Clear",
    command=clear_notes,
    width=20
)

clear_btn.pack(pady=5)

window.mainloop()
