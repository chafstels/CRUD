import datetime


def log_activity(func):
    def wrapper(self, *args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arguments = ", ".join(
            [repr(arg) for arg in args]
            + [f"{key}={repr(value)}" for key, value in kwargs.items()]
        )
        print(f"[{timestamp}] Вызов метода {func.__name__}({arguments})")
        return func(self, *args, **kwargs)

    return wrapper


class Task:
    def __init__(self, title, description, status="не выполнено"):
        self.title = title
        self.description = description
        self.status = status
        self.creation_date = datetime.datetime.now().strftime("%Y-%m-%d")

    @log_activity
    def mark_as_done(self):
        self.status = "выполнено"

    @log_activity
    def mark_as_undone(self):
        self.status = "не выполнено"

    @log_activity
    def edit_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f"Название: {self.title}\nОписание: {self.description}\nСтатус: {self.status}\nДата создания: {self.creation_date}\n"


class TaskList:
    def __init__(self):
        self.tasks = []

    @log_activity
    def create_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    @log_activity
    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        else:
            return None

    @log_activity
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    @log_activity
    def get_all_tasks(self):
        return self.tasks

    def __len__(self):
        return len(self.tasks)


task_list = TaskList()

task_list.create_task("Покупки", "Купить продукты")
task_list.create_task("Уборка", "Убрать комнату")
task_list.create_task("Учеба", "Подготовиться к экзамену")

task_list.get_task(1).mark_as_done()
task_list.get_task(2).edit_description("Подготовиться к экзамену по математике")

tasks = task_list.get_all_tasks()
for task in tasks:
    print(task)

task_list.remove_task(0)

print(len(task_list))
