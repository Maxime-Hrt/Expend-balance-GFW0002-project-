# Dictionary to stock every balance depends of the person 
expenses = {}
expenses_balance = {}

# Function to remove an expense
def remove_expense(name, amount):
  if name not in expenses:
    print(f"{name} isn't in the application list yet, you might have miss typing")
    return
  expenses[name] -= amount
  if expenses[name] == 0:
    del expenses[name]


# function to add an expense
def add_expense(name, amount):
  if name not in expenses:
    print(f"A new profile for {name} has been created")
    expenses[name] = 0

  expenses[name] += amount


# Function to show the balance of every person
def show_balances():
  total_expenses = 0
  for name, amount in expenses.items():
    total_expenses += amount
    print(f"{name}: {amount}")
  print(f"Total: {total_expenses}")

# Function to split each values by the average value
def even_split():
  total_expenses = sum(expenses.values())
  nb_people = len(expenses)
  even_split = total_expenses / nb_people
  for name, amount in expenses.items():
    expenses[name] = even_split

# Function to save data in a text file
def save_expenses(filename):
  with open(filename, "w") as f:
    for name, amount in expenses.items():
      f.write(f"{name},{amount}\n")

# Function to load data from a file
def load_expenses(filename):
  with open(filename, "r") as f:
    for line in f:
      name, amount = line.strip().split(",")
      expenses[name] = float(amount)

# Function to show how much everyone have to pay or get
def show_equitable_balance():
    total = sum(expenses.values()) 
    number = len(expenses)
    average = total/number #get the average
    for name, amount in expenses.items():
        expenses_balance[name] = amount-int(average) #add in a new dictionary, everyone's expend, minus the average
        if expenses_balance[name] > 0: #if the value minus the average > 0, it means that the person has to receive money
            print(f"{name} has to receive {expenses_balance[name]}")
        else:
            print(f"{name} has to pay {abs(expenses_balance[name])}") 
        

#Menu to switch between different cases
def menu():
    choice = input(
        " \n\nPlease enter:\n\t 1: Add an expense (and someone if the profile is not created yet) \n\t 2: Remove an expense \n\t 3: Show how much everyone paid \n\t 4: Show how much everyone have to paid or receive \n\t 5: Save expenses (in txt file) \n\t 6: Quit \n "
    )
    return int(choice) #convert the input to a int


# -----------------------------------------------Main Loop-----------------------------------------------------------
end = 1 #If end = 0, leave the game

while end:   
    choice = menu()

    if choice == 1:
        name_ = input("Who paid ?\n")
        amount_ = input("For how much ?\n")
        add_expense(name_, int(amount_))
    
    if choice == 2:
        name_ = input("From who an expense should be removed ?\n")
        amount_ = input("How much have to be removed ?\n")
        remove_expense(name_, int(amount_))

    if choice == 3:
        show_balances()

    if choice == 4:
        show_equitable_balance()

    if choice == 5:
        save_expenses()

    if choice == 6:
        end=0