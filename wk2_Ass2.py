todo_list = []  # This will hold all the user's tasks.

while True:
    print("\n--- TODO LIST MENU ---")
    print("C: Create | V: View | U: Update | D: Delete | Q: Quit")
    choice = input("Select an action: ").lower()

    # CREATE
    if choice == 'c':
        task = {
            "ToDo": input("Enter Task Name: "),
            "Details": input("Enter Task Description: "),
            "Status": input("Enter Status (e.g., Pending, Done): ")
        }
        todo_list.append(task)
        print("Task added successfully!")

    # VIEW
    elif choice == 'v':
        if not todo_list:
            print("The list is empty.")
        else:
            for index, task in enumerate(todo_list):
                print(f"{index}. {task['ToDo']} | {task['Details']} | Status: {task['Status']}\n")

    # UPDATE
    elif choice == 'u':
        if not todo_list:
            print("Nothing to update.")
            continue
        
        idx = int(input("Enter the task number to update: ")) #To identify what task in the list
        if 0 <= idx < len(todo_list): #within available list
            print("What would you like to update? (1: Name, 2: Details, 3: Status)")
            sub_choice = input() #Know what in the dictionary needs to change
            if sub_choice == '1':
                todo_list[idx]['ToDo'] = input("New Name: ")
            elif sub_choice == '2':
                todo_list[idx]['Details'] = input("New Details: ")
            elif sub_choice == '3':
                todo_list[idx]['Status'] = input("New Status: ")
            print("Task updated!")
        else:
            print("Invalid task number.")

    # DELETE
    elif choice == 'd':
        idx = int(input("Enter the task number to delete: "))
        if 0 <= idx < len(todo_list):
            removed = todo_list.pop(idx)
            print(f"Deleted: {removed['ToDo']}")
        else:
            print("Invalid task number.")

    # QUIT
    elif choice == 'q':
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
