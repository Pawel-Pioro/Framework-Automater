from threading import Thread

import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont
from tkinter import ttk

from scripts.main import django_project, react_project, go_project

# setup
root = tk.Tk()
root.title("Framework Automater")

# variables
FRAMEWORK_OPTIONS = ["Django", "React", "GO"]
folder_path = tk.StringVar()
selected_framework = tk.StringVar()
project_name = tk.StringVar()
error = tk.StringVar()
status = tk.StringVar()

# functions
def execute_command(framework, path, name):
    if framework == "Django":
        django_project(path, name)
    elif framework == "React":
        react_project(path, name)
    elif framework == "GO":
        go_project(path, name)

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def validate(selected_framework, folder_path, project_name):
    selected_framework, folder_path, project_name = selected_framework.get(), folder_path.get(), project_name.get()
    if selected_framework and folder_path and project_name:
        error.set("")
        status.set("Creating project...")
        execute_command(selected_framework, folder_path, project_name)
    else:
        error.set("Please select a framework, a name and a folder path!")

# Error message
error_label = tk.Label(root, textvariable=error, fg="red")
error_label.pack()

# Title
heading_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
heading_label = tk.Label(root, text="Framework Automater", font=heading_font)
heading_label.pack(pady=(20, 10))

# dropdown menu
dropdown_frame = tk.Frame(root)
dropdown_frame.pack(pady=(10, 20), padx=20, fill=tk.X)
dropdown_label = tk.Label(dropdown_frame, text="Select an option:")
dropdown_label.pack(side=tk.LEFT)
dropdown_menu = ttk.Combobox(dropdown_frame, textvariable=selected_framework , state="readonly")
dropdown_menu['values'] = FRAMEWORK_OPTIONS
dropdown_menu.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)

# project name
project_frame = tk.Frame(root)
project_frame.pack(pady=(10, 20), padx=20, fill=tk.X)
project_name_label = tk.Label(project_frame, text="Enter project name:")
project_name_label.pack(side=tk.LEFT)
project_name_entry = tk.Entry(project_frame, textvariable=project_name)
project_name_entry.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)

# folder selection
frame = tk.Frame(root)
frame.pack(pady=(10, 20), padx=20, fill=tk.X)
browse_button = tk.Button(frame, text="Select Folder Path", command=browse_folder)
browse_button.pack(side=tk.LEFT)
folder_entry = tk.Entry(frame, textvariable=folder_path, state='readonly', width=50)
folder_entry.pack(side=tk.LEFT, padx=(10, 0), fill=tk.X, expand=True)

# run button
run_button = tk.Button(root, textvariable=status, command=Thread(target=validate, args=(selected_framework, folder_path, project_name)).start)
run_button.pack(pady=(10, 20))

root.mainloop()