#Define properties
class Task:
    def __init__(self, name, details, status):
        self.name = name
        self.details = details
        self.status = status

    def __str__(self):
        return f"{self.name} | {self.details} | Status: {self.status}"
class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input("Enter Task Name: ")
        details = input("Enter Task Description: ")
        status = input("Enter Status: ")
        new_task = Task(name, details, status)
        self.tasks.append(new_task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("The list is empty.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index}. {task}") 

    def update_task(self):
        self.view_tasks()
        if not self.tasks: return
        
        try:
            idx = int(input("Enter task number to update: "))
            task = self.tasks[idx]
            print("1: Name | 2: Details | 3: Status")
            choice = input("Choice: ")
            
            if choice == '1': task.name = input("New Name: ")
            elif choice == '2': task.details = input("New Details: ")
            elif choice == '3': task.status = input("New Status: ")
            print("Updated!")
        except (ValueError, IndexError):
            print("Invalid input or task number.")

    def delete_task(self):
        try:
            idx = int(input("Enter task number to delete: "))
            removed = self.tasks.pop(idx)
            print(f"Deleted: {removed.name}")
        except (ValueError, IndexError):
            print("Invalid task number.")

# --- Run The Program ---
manager = TodoManager()

while True:
    print("\n--- TODO CLASS MENU ---")
    print("C: Create | V: View | U: Update | D: Delete | Q: Quit")
    choice = input("Select an action: ").lower()

    if choice == 'c': manager.add_task()
    elif choice == 'v': manager.view_tasks()
    elif choice == 'u': manager.update_task()
    elif choice == 'd': manager.delete_task()
    elif choice == 'q':
        print("Goodbye!")
        break