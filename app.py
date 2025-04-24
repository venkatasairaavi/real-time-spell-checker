# app.py

import tkinter as tk
from tkinter import ttk 

# main window
root = tk.Tk() 
root.title("Real-Time Spell Checker")
root.geometry("600x400")

# text input field
text_area = tk.Text(root, font=("Arial", 14), wrap="word")
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# spell check button
def check_spelling():
    content = text_area.get("1.0", tk.END)
    print("Content to check: ", content)

check_button = ttk.Button(root, text="Check Spelling", command=check_spelling)
check_button.pack(pady=10)

# run the application
root.mainloop()