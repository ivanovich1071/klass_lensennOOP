class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # По умолчанию задача не выполнена

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена.")

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = True
                print(f"Задача '{description}' выполнена.")
                return
        print(f"Задача '{description}' не найдена.")

    def list_current_tasks(self, include_completed=False):
        print("Текущие задачи:")
        for task in self.tasks:
            if include_completed or not task.status:
                print(f"- {task.description} (Срок: {task.deadline}, Статус: {'выполнена' if task.status else 'не выполнена'})")


task_manager = TaskManager()

#  ввод задач и времени выполнения
tasks_count = 0
while tasks_count < 20:
    description = input("Введите описание задачи (или 'esc', чтобы закончить ввод): ")
    if description.lower() == "esc":
        break
    deadline = input("Введите время выполнения задачи (например, 09:00): ")
    task_manager.add_task(description, deadline)
    tasks_count += 1

#  отметкф задач как выполненных или не выполненных
while True:
    choice = input("Отметить задачу как выполненную (v) или как не выполненную (n)? Введите 'exit' для завершения: ")
    if choice.lower() == "exit":
        break
    if choice.lower() == "v" or choice.lower() == "n":
        task_description = input("Введите описание задачи: ")
        if choice.lower() == "v":
            task_manager.mark_completed(task_description)
        else:
            task_manager.mark_completed(task_description)

    # Вывод списков задач каждый час
    import time
    hour = 4800  #  в секундах(для примерф 5 минут)
    while True:
        print("\n---" + time.strftime("%H:%M:%S") + "---")
        task_manager.list_current_tasks(include_completed=True)
        print("\n")
        task_manager.list_current_tasks()
        time.sleep(hour)