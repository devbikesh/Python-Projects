tasks = []

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Edit Task")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        task_count = int(input("How many tasks do you want to add? "))

        for task_number in range(task_count):
            task_name = input("Enter the task: ")
            tasks.append(task_name)
            print("Task Added!")

    elif choice == 2:

        if tasks == []:
            print("No Tasks Available.")

        else:
            print("\nYour Tasks:")

            for task_number in range(len(tasks)):
                print(f"{task_number + 1}. {tasks[task_number]}")

            print("Total Tasks:", len(tasks))

    elif choice == 3:

        if tasks == []:
            print("No Tasks Available.")

        else:
            print("\nYour Tasks:")

            for task_number in range(len(tasks)):
                print(f"{task_number + 1}. {tasks[task_number]}")

            task_number = int(input("Which task do you want to remove? "))

            if task_number >= 1 and task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("Task Removed!")

            else:
                print("Invalid Task Number!")

    elif choice == 4:

        while True:

            print("\n1. Change Task Name")
            print("2. Back")

            edit_choice = int(input("Enter your choice: "))

            if edit_choice == 1:

                if tasks == []:
                    print("No Tasks Available.")

                else:
                    print("\nYour Tasks:")

                    for task_number in range(len(tasks)):
                        print(f"{task_number + 1}. {tasks[task_number]}")

                    task_number = int(
                        input("Which task do you want to edit? ")
                    )

                    if task_number >= 1 and task_number <= len(tasks):

                        new_task_name = input(
                            "Enter the new task name: "
                        )

                        tasks[task_number - 1] = new_task_name

                        print("Task Updated!")

                    else:
                        print("Invalid Task Number!")

            elif edit_choice == 2:
                break

            else:
                print("Invalid Choice!")

    elif choice == 5:

        print("Goodbye!")
        break

    else:

        print("Invalid Choice!")