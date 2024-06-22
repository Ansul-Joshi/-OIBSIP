import tkinter as tk
from tkinter import simpledialog
import random

def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = int(letter_entry.get())
    nr_symbols = int(symbol_entry.get())
    nr_numbers = int(number_entry.get())

    password_chars = random.choices(letters, k=nr_letters) + \
                     random.choices(numbers, k=nr_numbers) + \
                     random.choices(symbols, k=nr_symbols)

    random.shuffle(password_chars)
    password = ''.join(password_chars)
    result_label.config(text=password)

root = tk.Tk()
root.title("Password Generator")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

tk.Label(root, text="Number of Letters:").grid(row=0, column=0)
letter_entry = tk.Entry(root)
letter_entry.grid(row=0, column=1)

tk.Label(root, text="Number of Symbols:").grid(row=1, column=0)
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=1, column=1)

tk.Label(root, text="Number of Numbers:").grid(row=2, column=0)
number_entry = tk.Entry(root)
number_entry.grid(row=2, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="", font=('Helvetica', 12, 'bold'))
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
