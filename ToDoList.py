tasks = []

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date: ")
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    task_index = int(input("Enter the index of the task to remove: "))
    if task_index >= 0 and task_index < len(tasks):
        del tasks[task_index]
        print("Task removed successfully!")
    else:
        print("Invalid task index!")

def mark_task_completed():
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index!")

def display_tasks():
    for index, task in enumerate(tasks):
        print(f"Task #{index}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Status: {'Completed' if task['completed'] else 'Not Completed'}")
        print()

def main():
    while True:
        print("To-Do List")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()