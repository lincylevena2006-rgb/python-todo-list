def show_tasks(tasks):
    print("\n========== YOUR TASKS ==========")

    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter a new task: ")

    if task.strip():
        tasks.append(task)
        print("Task added successfully! ✅")
    else:
        print("Task cannot be empty!")


def remove_task(tasks):
    show_tasks(tasks)

    if tasks:
        try:
            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Task removed: {removed} 🗑️")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number.")


tasks = []

print("================================")
print("        TO-DO LIST MANAGER")
print("================================")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        remove_task(tasks)

    elif choice == "4":
        print("\nThank you for using To-Do List Manager! 👋")
        break

    else:
        print("Invalid choice!")