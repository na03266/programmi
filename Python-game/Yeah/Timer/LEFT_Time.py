import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk

# create a tkinter window
window = tk.Tk()
window.title("Time Calculator")
window.geometry("600x400")
window.resizable(False, False)
window.configure(background="#F0F0F0")

# create a style for the labels and buttons
style = ttk.Style()
style.configure("TLabel", font=("Arial", 14), padding=5, background="#F0F0F0")
style.configure("TButton", font=("Arial", 14), padding=5, background="#4CAF50", foreground="white", borderwidth=0)

# create a label and DateEntry widget for the user to select the future date
date_label = ttk.Label(window, text="Select a future date:")
date_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)
date_entry = DateEntry(window, width=12, font=("Arial", 14), background='#E0E0E0', foreground='black', borderwidth=0)
date_entry.grid(row=0, column=1, padx=10, pady=10)

# create a label to display the remaining time
result_label = ttk.Label(window, text="", font=("Arial", 18), background="#F0F0F4")
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

# load the image and create a resizable label to display it
image = Image.open("example.png")
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(window, image=photo, background="#F0F0F0")
image_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

