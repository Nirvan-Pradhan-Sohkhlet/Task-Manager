import os

TASKS_FILE = "tasks.txt"

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"
    
    def from_string(line):
        parts = line.strip().split('|')
        description = parts[0]
        completed = parts[1] == 'True'
        return Task(description, completed)

    def to_string(self):
        return f"{self.description}|{self.completed}"

class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Added task: {description}")

    def edit_task(self, task_index, new_description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description
            print(f"Edited task to: {new_description}")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f"Deleted task: {deleted_task.description}")
        else:
            print("Invalid task number.")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f"Marked task as complete: {self.tasks[task_index].description}")
        else:
            print("Invalid task number.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Task List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            for task in self.tasks:
                f.write(task.to_string() + "\n")
        print("Tasks saved to file.")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                self.tasks = [Task.from_string(line) for line in f.readlines()]
            print("Tasks loaded from file.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Display Tasks")
        print("6. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            task_index = int(input("Enter task number to edit: ")) - 1
            new_description = input("Enter new description: ")
            todo_list.edit_task(task_index, new_description)
        elif choice == "3":
            task_index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter task number to mark as complete: ")) - 1
            todo_list.mark_task_complete(task_index)
        elif choice == "5":
            todo_list.display_tasks()
        elif choice == "6":
            todo_list.save_tasks()
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

main()