import tkinter as tk

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Не выполнено"

tasks = []

def add_task():
    task_description = task_entry.get()
    task_deadline = deadline_entry.get()
    if task_description and task_deadline:
        task = Task(task_description, task_deadline)
        tasks.append(task)
        assigned_tasks_listBox.insert(tk.END, f"{len(tasks)}. {task_description} - до {task_deadline}")
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)

def mark_as_done():
    selected_task_index = assigned_tasks_listBox.curselection()
    if selected_task_index:
        selected_task = tasks[selected_task_index[0]]
        selected_task.status = "Выполнено"
        done_tasks_listBox.insert(tk.END, f"{selected_task.description} - до {selected_task.deadline}")
        assigned_tasks_listBox.delete(selected_task_index)

root = tk.Tk()
root.title("Управление задачами")
root.configure(background="DarkSeaGreen3")

text1 = tk.Label(root, text="Введите вашу задачу и срок выполнения:", bg="DarkSeaGreen3")
text1.grid(row=0, column=0, columnspan=20, pady=25)

task_entry = tk.Entry(root, width=50, bg="DarkSlateBlue")
task_entry.grid(row=1, column=0, columnspan=20, pady=5, padx=25)

deadline_entry = tk.Entry(root, width=20, bg="DarkSlateBlue")
deadline_entry.grid(row=1, column=3, pady=5)

add_task_button = tk.Button(root, text="Добавить задачу", bg="DarkSeaGreen4", command=add_task)
add_task_button.grid(row=2, column=0, pady=5)

mark_as_done_button = tk.Button(root, text="Отметить как выполненное", bg="DarkSeaGreen4", command=mark_as_done)
mark_as_done_button.grid(row=2, column=1, columnspan=3, pady=5)

assigned_text = tk.Label(root, text="Назначенные задачи:", bg="DarkSeaGreen3")
assigned_text.grid(row=3, column=0, pady=5)
assigned_tasks_listBox = tk.Listbox(root, height=10, width=50, bg="DarkOrchid")
assigned_tasks_listBox.grid(row=4, column=0, columnspan=4, pady=5, padx=10)

done_text = tk.Label(root, text="Выполненные задачи:", bg="DarkSeaGreen3")
done_text.grid(row=5, column=0, pady=5)
done_tasks_listBox = tk.Listbox(root, height=10, width=50, bg="light green")
done_tasks_listBox.grid(row=6, column=0, columnspan=4, pady=5, padx=10)

root.grid_rowconfigure(0, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

def show_tasks_status():
    for task in tasks:
        print(f"{tasks.index(task) + 1}. {task.description} - до {task.deadline} - {task.status}")

def check_tasks_completion():
    done_tasks_listBox.delete(0, tk.END)
    assigned_tasks_listBox.delete(0, tk.END)

    for task in tasks:
        if task.status == "Выполнено":
            done_tasks_listBox.insert(tk.END, f"{task.description} - до {task.deadline}")
        else:
            assigned_tasks_listBox.insert(tk.END, f"{tasks.index(task) + 1}. {task.description} - до {task.deadline}")

check_tasks_completion()

root.after(3600000, check_tasks_completion)  # 1 hour = 3600000 milliseconds
root.mainloop()