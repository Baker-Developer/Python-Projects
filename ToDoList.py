import tkinter as tk
from tkcalendar import DateEntry

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create a list to store the tasks
tasks = []

# Create a function to add a task
def add_task():
    # Get the task and due date from the entry boxes
    task = task_entry.get()
    due_date = due_date_entry.get_date()
    # Add the task and due date to the list as a tuple
    tasks.append((task, due_date))
    # Clear the entry boxes
    task_entry.delete(0, "end")
    due_date_entry.set_date(None)
    # Update the listbox with the new task
    update_listbox()

# Create a function to update the listbox
def update_listbox():
    # Clear the listbox
    listbox.delete(0, "end")
    # Loop through the tasks and add them to the listbox
    for task in tasks:
        listbox.insert("end", task[0] + " - " + task[1].strftime("%m/%d/%Y"))

# Create a function to delete a task
def delete_task():
    # Get the selected task
    selected_task = listbox.get("active")
    # Remove the task from the list
    tasks.remove(selected_task)
    # Update the listbox
    update_listbox()

# Create a label and entry box for the task
task_label = tk.Label(text="Task:")
task_entry = tk.Entry(width=30)
task_label.pack()
task_entry.pack()

# Create a label and DateEntry widget for the due date
due_date_label = tk.Label(text="Due Date:")
due_date_entry = DateEntry(width=30)
due_date_label.pack()
due_date_entry.pack()

# Create a button to add the task
add_button = tk.Button(text="Add Task", command=add_task)
add_button.pack()

# Create a listbox to display the tasks
listbox = tk.Listbox(width=30)
listbox.pack()

# Create a button to delete a task
delete_button = tk.Button(text="Delete Task", command=delete_task)
delete_button.pack()

# Run the main loop
window.mainloop()
