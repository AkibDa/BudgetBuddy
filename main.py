print("Welcome to BudgetBuddy!")

def savings(income, expenses):
  savings = income - expenses
  print("You have Rs " + str(savings) + " left over each month.")
  choice = input("Would you like to save or spend this money? (save/spend): ")
  if choice == "save":
      savings += float(input("How much would you like to save? "))
      print("You now have Rs " + str(savings) + " saved.")
  elif choice == "spend":
      savings -= float(input("How much would you like to spend? "))
      print("You now have Rs " + str(savings) + " left over.")
  else:
      print("Invalid choice. Please try again.")
      

  if savings <= 0:
      print("You have run out of money!")
  else:
      print("You have Rs " + str(savings) + " left over.")
      print("Thank you for using BudgetBuddy!")
  
def add_transaction(date, category, amount, description, type):
  print("Transaction added successfully!")
  print("Date: " + date)
  print("Category: " + category)
  print("Amount: " + str(amount))
  print("Description: " + description)
  print("Type: " + type)
  print("Thank you for using BudgetBuddy!")
  
def view_balance(income, expenses):
  print(f"Income: Rs {income}")
  print(f"Expenses: Rs {expenses}")
  print(f"Balance: Rs {income-expenses}")
  print("Thank you for using BudgetBuddy!")
  
def advice():
  print("Advice: ")
  print("Thank you for using BudgetBuddy!")

while True:
  
  income = float(input("Please enter your monthly income: "))
  expenses = float(input("Please enter your monthly expenses: "))
  
  if income < expenses:
    print("Your expenses are greater than your income. Please try again.")
    break
  elif income == expenses:
    print("Your expenses are equal to your income. You have no money left over.")
    break
  elif income == 0 or expenses == 0:
    print("You have no income or expenses. You have no money left over.")
    break
  else:
    print("1. Add Transaction")
    print("2. View Balance")
    print("3. Calculate Savings")
    print("4. Need advice?")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
      date = input("Date (YYYY-MM-DD): ")
      category = input("Category: ")
      amount = float(input("Amount: "))
      description = input("Description: ")
      type = input("Type (income/expense): ")
      add_transaction(date, category, amount, description, type)
      break
    elif choice == "2":
      view_balance(income, expenses)
      break
    elif choice == "3":
      savings(income, expenses)
      break
    elif choice == "4":
      advice()
      break
    elif choice == "5": 
      print("Thank you for using BudgetBuddy!")
      break
    else:
      print("Invalid choice. Please try again.")
      break