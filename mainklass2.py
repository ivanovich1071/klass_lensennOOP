class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # По умолчанию задача не выполнена


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_counter = 1

    def add_task(self, description, deadline):
        task = Task(f"{self.task_counter}. {description}", deadline)
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена.")
        self.task_counter += 1

    def mark_completed(self, task_number):
        for task in self.tasks:
            if task.description.startswith(f"{task_number}."):
                task.status = True
                print(f"Задача '{task.description[3:]}' выполнена.")
                return
        print(f"Задача с порядковым номером {task_number} не найдена.")

    def list_current_tasks(self, include_completed=False):
        print("Текущие задачи:")
        for task in self.tasks:
            if include_completed or not task.status:
                print(f"- {task.description[3:]} (Срок: {task.deadline}, Статус: {'выполнена' if task.status else 'не выполнена'})")


task_manager = TaskManager()

# Ввод задач и времени выполнения
tasks_count = 0
while tasks_count < 20:
    description = input("Введите описание задачи (или 'done', чтобы закончить ввод): ")
    if description.lower() == "done":
        break
    deadline = input("Введите срок выполнения задачи (например, 15:00): ")
    task_manager.add_task(description, deadline)
    tasks_count += 1

# Отметка задач как выполненных или не выполненных
while True:
    choice = input("Отметить задачу как выполненную (v) или как не выполненную (n)? Введите 'exit' для завершения: ")
    if choice.lower() == "exit":
        break
    if choice.lower() == "v" or choice.lower() == "n":
        task_number = input("Введите порядковый номер задачи: ")
        if choice.lower() == "v":
            task_manager.mark_completed(task_number)
        else:
            task_manager.mark_completed(task_number)

    # Вывод списков задач ( при демонстрации 5 минут)
    import time
    hour = 300  # ( демо - 5 минут)1 час в секундах
    while True:
        print("\n---" + time.strftime("%H:%M") + "---")
        task_manager.list_current_tasks(include_completed=True)
        print("\n")
        task_manager.list_current_tasks()
        time.sleep(hour)