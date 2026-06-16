total = 0
count = 0

print("Welcome to the expense tracker!")
print("Enter your expenses . Type 'Quit' or 'Exit' to stop.")
print("===================================")
while True:
    expense = input("Enter expense amount : ")
    if expense.lower() == "done" or expense.lower() == "quit":
        break
    if expense == "":
        print("Input cannot be empty. Please enter a number.\n")
        continue
    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative. Please enter a valid amount.\n")
            continue

        total += expense
        count += 1

        print(f"Expense added: ₹{expense:.2f}")
        print(f"Current total: ₹{total:.2f}\n")

    except ValueError:
        print("Please enter a valid number.\n")
if count > 0:
    Average = total / count
    print("     FINAL REPORT    ")
    print("===================================")
    print(f"Total expenses: ₹{total:.2f}")
    print(f"Average expense: ₹{Average:.2f}")
    print(f"Number of expenses entered: {count}")
else:
    print("No expenses entered.")   
print("Expense tracker ended successfully!")

