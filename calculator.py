import tkinter as tk
import math

# Define the functions


def calculate_log():
    number = float(number_entry.get())
    base = float(base_entry.get())
    result = math.log(number, base)
    result_label.config(text=f"Result: {result}")


def convert_to_binary():
    number = int(number_entry.get())
    binary = bin(number)[2:]
    result_label.config(text=f"Result: {binary}")


# Create the GUI
root = tk.Tk()
root.title("Calculator")

# Create the widgets
number_label = tk.Label(root, text="Number:")
number_entry = tk.Entry(root)
base_label = tk.Label(root, text="Base:")
base_entry = tk.Entry(root)
log_button = tk.Button(root, text="Log", command=calculate_log)
binary_button = tk.Button(
    root, text="Decimal to Binary", command=convert_to_binary)
result_label = tk.Label(root, text="Result:")

# Layout the widgets
number_label.grid(row=0, column=0)
number_entry.grid(row=0, column=1)
base_label.grid(row=1, column=0)
base_entry.grid(row=1, column=1)
log_button.grid(row=2, column=0)
binary_button.grid(row=2, column=1)
result_label.grid(row=3, column=0, columnspan=2)

# Run the GUI
root.mainloop()
