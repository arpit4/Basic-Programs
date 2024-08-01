class TodoList:
    def __init__(self):
        self.tasks = {}

    def display_tasks(self):
        print("\nTo-Do List:")
        for task, status in self.tasks.items():
            print(f"{task}: {status}")

    def add_task(self, task):
        self.tasks[task] = "Not Started"
        print(f"Task '{task}' added!")

    def delete_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' deleted!")
        else:
            print(f"Task '{task}' not found!")

    def mark_as_done(self, task):
        if task in self.tasks:
            self.tasks[task] = "Done"
            print(f"Task '{task}' marked as done!")
        else:
            print(f"Task '{task}' not found!")

def main():
    todo = TodoList()

    while True:
        print("\nOptions:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark as Done")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            todo.display_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "3":
            task = input("Enter task to delete: ")
            todo.delete_task(task)
        elif choice == "4":
            task = input("Enter task to mark as done: ")
            todo.mark_as_done(task)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

