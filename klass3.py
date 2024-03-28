import tkinter as tk
from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "не выполнено"

tasks = []

def add_task():
    description = task_entry.get()
    deadline = deadline_entry.get()
    if description and deadline:
        task = Task(description, deadline)
        tasks.append(task)
        assigned_tasks_listBox.insert(tk.END, f"{len(tasks)} - {task.description}")
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)

def mark_as_done():
    selected_task = assigned_tasks_listBox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task = tasks[task_index]
        task.status = "выполнено"
        assigned_tasks_listBox.delete(selected_task)
        assigned_tasks_listBox.insert(tk.END, f"{task_index + 1} - {task.description} - {task.status}")

def update_lists():
    in_progress_tasks_listBox.delete(0, tk.END)
    done_tasks_listBox.delete(0, tk.END)
    for task in tasks:
        if task.status == "не выполнено":
            in_progress_tasks_listBox.insert(tk.END, f"{task.description} - {task.deadline}")
        else:
            done_tasks_listBox.insert(tk.END, f"{task.description} - {task.deadline}")

def hourly_update():
    current_time = datetime.now().strftime("%H:%M")
    if current_time[-2:] == "00":
        update_lists()
    root.after(1000 * 60 * 60, hourly_update)  # 1 час = 3600000 миллисекунд

root = tk.Tk()
root.title("Управление задачами")
root.configure(background="DarkSeaGreen3")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="DarkSeaGreen3")
text1.grid(row=0, column=0, pady=5)
task_entry = tk.Entry(root, width=50, bg="DarkSlateBlue")
task_entry.grid(row=1, column=0, pady=5, padx=10)

text2 = tk.Label(root, text="Введите срок выполнения (чч:мм):", bg="DarkSeaGreen3")
text2.grid(row=2, column=0, pady=5)
deadline_entry = tk.Entry(root, width=50, bg="DarkSlateBlue")
deadline_entry.grid(row=3, column=0, pady=5, padx=10)

add_task_button = tk.Button(root, text="Добавить задачу", bg="DarkSeaGreen4", command=add_task)
add_task_button.grid(row=4, column=0, pady=5)

mark_as_done_button = tk.Button(root, text="Пометить как выполненное", bg="DarkSeaGreen4", command=mark_as_done)
mark_as_done_button.grid(row=4, column=1, pady=5)

assigned_text = tk.Label(root, text="Назначенные задачи:", bg="DarkSeaGreen3")
assigned_text.grid(row=5, column=0, pady=5)
assigned_tasks_listBox = tk.Listbox(root, height=10, width=50, bg="DarkOrchid")
assigned_tasks_listBox.grid(row=6, column=0, columnspan=2, pady=5, padx=10)

in_progress_text = tk.Label(root, text="Задачи в работе:", bg="DarkSeaGreen3")
in_progress_text.grid(row=5, column=2, pady=5)
in_progress_tasks_listBox = tk.Listbox(root, height=10, width=50, bg="light blue")
in_progress_tasks_listBox.grid(row=6, column=2, pady=5, padx=10)

done_text = tk.Label(root, text="Выполненные задачи:", bg="DarkSeaGreen3")
done_text.grid(row=5, column=3, pady=5)
done_tasks_listBox = tk.Listbox(root, height=10, width=50, bg="light green")
done_tasks_listBox.grid(row=6, column=3, pady=5, padx=10)

update_lists()
hourly_update()

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()