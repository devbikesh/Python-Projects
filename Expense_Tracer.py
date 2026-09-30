expenses = {}

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Remove Expense")
    print("5. Edit Expense")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Expense
    if choice == 1:

        expense_count = int(
            input("How many expenses do you want to add? ")
        )

        for expense_number in range(expense_count):

            expense_name = input("Enter the expense name: ")
            expense_amount = int(input("Enter the amount: "))

            expenses[expense_name] = expense_amount

        print("Expenses added!")

    # View Expenses
    elif choice == 2:

        if expenses == {}:
            print("No expenses available.")

        else:
            print("\nYour Expenses:")

            expense_number = 1

            for expense_name, expense_amount in expenses.items():

                print(
                    f"{expense_number}. "
                    f"{expense_name}: {expense_amount}"
                )

                expense_number += 1

            print("Total Expenses:", len(expenses))

    # Show Total
    elif choice == 3:

        total_amount = 0

        for expense_name, expense_amount in expenses.items():
            total_amount += expense_amount

        print("Total amount:", total_amount)

    # Remove Expense
    elif choice == 4:

        if expenses == {}:
            print("No expenses available.")

        else:
            print("\nYour Expenses:")

            expense_number = 1

            for expense_name, expense_amount in expenses.items():

                print(
                    f"{expense_number}. "
                    f"{expense_name}: {expense_amount}"
                )

                expense_number += 1

            remove_number = int(
                input("Which expense do you want to remove? ")
            )

            expense_number = 1
            expense_to_remove = None

            for expense_name, expense_amount in expenses.items():

                if expense_number == remove_number:
                    expense_to_remove = expense_name
                    break

                expense_number += 1

            if expense_to_remove is not None:

                expenses.pop(expense_to_remove)
                print("Expense removed!")

            else:
                print("Invalid expense number.")

    # Edit Expense
    elif choice == 5:

        if expenses == {}:
            print("No expenses available.")

        else:
            print("\nYour Expenses:")

            expense_number = 1

            for expense_name, expense_amount in expenses.items():

                print(
                    f"{expense_number}. "
                    f"{expense_name}: {expense_amount}"
                )

                expense_number += 1

            edit_number = int(
                input("Which expense do you want to edit? ")
            )

            expense_number = 1
            expense_to_edit = None

            for expense_name, expense_amount in expenses.items():

                if expense_number == edit_number:
                    expense_to_edit = expense_name
                    break

                expense_number += 1

            if expense_to_edit is not None:

                new_expense_name = input(
                    "Enter the new expense name: "
                )

                new_expense_amount = int(
                    input("Enter the new amount: ")
                )

                expenses.pop(expense_to_edit)

                expenses[new_expense_name] = new_expense_amount

                print("Expense updated!")

            else:
                print("Invalid expense number.")

    # Exit
    elif choice == 6:

        print("Thank you :)")
        break

    else:
        print("Invalid choice!")