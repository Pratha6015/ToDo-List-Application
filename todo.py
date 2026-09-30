import os

FILENAME = "todo_list.txt"

def load_tasks():
    """Load tasks from the text file if it exists."""
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

def save_tasks(tasks):
    """Save the current list of tasks to the text file."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display all current tasks."""
    if not tasks:
        print("\nYour to-do list is empty! 🎉")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("-" * 23)

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== TO-DO LIST APP ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            show_tasks(tasks)
            
        elif choice == '2':
            new_task = input("Enter the new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"'{new_task}' added successfully!")
            else:
                print("Task cannot be empty.")
                
        elif choice == '3':
            show_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the number of the task to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"'{removed}' has been deleted.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == '4':
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()