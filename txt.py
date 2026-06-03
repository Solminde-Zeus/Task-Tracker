# We Import the Lib
import json
import os
import tkinter as tk
from tkinter import messagebox
# create a varbile so that no need to type much
FILENAME = "tasks.json"
#Function Making for the required Features 
def load_tasks():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def update_listbox():
#Refreshes the visual list of tasks on the screen.
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks, 1):
        status = "[COMPLETE]" if task["complete"] else "[ ]"
        task_listbox.insert(tk.END, f"{index}. {status} {task['name']}")

def add_task():
    name = task_entry.get().strip()
    if name:
        tasks.append({"name": name, "complete": False})
        save_tasks()
        update_listbox()
        task_entry.delete(0, tk.END) # Clear the input box
    else:
        messagebox.showwarning("Warning", "Task name cannot be empty!")

def complete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["complete"] = True
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task from the list first!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

tasks = load_tasks()

#Working on UI
root = tk.Tk()
root.title("OG Task Tracker")
root.geometry("700x750")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text=" OG Task Tracker", font=("Arial", 50, "bold"), bg="#1a7e40")
title_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=5)

task_entry = tk.Entry(input_frame, width=25, font=("Arial", 12))
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(input_frame, text="Add", command=add_task, bg="#4C804E", fg="white", font=("Arial", 10, "bold"))
add_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 11), selectbackground="#a6a6a6")
task_listbox.pack(pady=15)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)
complete_button = tk.Button(button_frame, text= "Complete", command=complete_task, bg="#3AAEB2", fg="white", font=("Arial", 10, "bold"))
complete_button.pack(side=tk.LEFT, padx=10)
delete_button = tk.Button(button_frame, text="Delete", command=delete_task, bg="#F7A39D", fg="white", font=("Arial", 10, "bold"))
delete_button.pack(side=tk.LEFT, padx=10)

update_listbox()
root.mainloop()
