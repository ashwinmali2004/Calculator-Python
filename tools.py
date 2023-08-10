import tkinter as tk
from tkinter import ttk

def open_file_manager():
    # Add functionality to open the file manager here
    print("Opening file manager...")

def show_about():
    # Add functionality to show the about section here
    print("Showing about section...")

root = tk.Tk()
root.title("Custom Title Bar")
root.geometry("400x300")

# Configure the window to remove the default title bar
root.overrideredirect(True)

# Create a custom title bar using the ttk module
title_bar = ttk.Frame(root)
title_bar.pack(side="top", fill="x")

# Create buttons for file manager and about section
file_manager_button = ttk.Button(title_bar, text="File Manager", command=open_file_manager)
file_manager_button.pack(side="left", padx=5)

about_button = ttk.Button(title_bar, text="About", command=show_about)
about_button.pack(side="left", padx=5)

# Add other widgets and content to the main window as needed
# ...

root.mainloop()
