#task list initialization
running_task = []
completed_task = []

#adding tasks
def add_task(task):
    running_task.append(task)
    print(f"The task {task} is added.")

#marking of completed tasks    
def marked_as_completed(TaskList):
    if 0 <= TaskList< len(running_task):
        complete_task = running_task.pop(TaskList)
        completed_task.append(complete_task)
        print(f"Task {complete_task} is marked as complete")
    else:
        print("an error has occurred, please try again.")

#task view
def display_task():
    print("Tasks in progress: ")
    for i, task in enumerate(running_task, 1):
        print(f"{i}. {task}")
    
    print("Completed tasks: ")
    for i, task in enumerate(completed_task, 1):
        print(f"{i}. {task}")
    
#main loop
while True:
    print("1. Add a task")
    print("2. Marked a task as complete")
    print("3. show the tasks")
    print("4. leave the program")

    choice = input("Choose one of the following options:")

    if choice == "Add a task":
        new_task = input("Add the task: ")
        add_task(new_task)
    elif choice == "Marked a task as complete: ":
        completed_tasklist= int(input("Enter the task number to mark: "))
        marked_as_completed(completed_tasklist - 1)
    elif choice == "view tasks":
        display_task()
    elif choice == "leave the program":
        print("The program will close")
        break
    else:
        print("Invalid option, choose an existing one")