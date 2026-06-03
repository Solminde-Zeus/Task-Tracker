import json
import os


FILENAME = "PastTasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("\n[Warning] Task file was corrupted. Starting with an empty list.")
            return []
    return []

def save_tasks(tasks):
    """Saves the current task list to the JSON file."""
    try:
        with open(FILENAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("\n[Error] Could not save tasks to disk.")

def show_menu():
    print("")
    print("\n--- TASK TRACKER ---")
    print("")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour task list is empty!")
        return
    
    print("\nYOUR TASKS:")
    for index, task in enumerate(tasks, 1):
        status = "[X]" if task["complete"] else "[ ]"
        print(f"{index}. {status} {task['name']}")

def add_task(tasks):
    name = input("\nEnter the task name: ").strip()
    if name:
        tasks.append({"name": name, "complete": False})
        save_tasks(tasks)  # Save changes
        print(f"Task '{name}' added successfully !")
    else:
        print("Task name cannot be empty.") 

def complete_task (tasks):
    view_tasks (tasks)
    if not tasks:
        return
    
    try:
        choice = int(input("\nEnter the number of the task to complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["complete"] = True
            save_tasks(tasks)  # Save changes k
            print(f"Task '{tasks[choice - 1]['name']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:print("Please enter a valid number.")

        
    if choice == "1":
            view_tasks(tasks)
    elif choice == "2":
            add_task(tasks)
    elif choice == "3":
            complete_task(tasks)
    elif choice == "4":
            delete_task(tasks)
    elif choice == "5":
            print("\nTasks saved. Goodbye!")
            break
    else:
            print("Invalid choice, please choose between 1 and 5.")

    if_name_== "_main_":
    main()

