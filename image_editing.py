from PIL import Image
from tkinter import filedialog
import tkinter as tk


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
img = Image.open(file_path)
