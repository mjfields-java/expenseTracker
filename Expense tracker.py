userBudget = float(input("Please enter how much you've budgeted"  " for the month: "))

moreExpenses = 'y'
userTotalExpenses = 0

while moreExpenses == 'y':
    userExpense = float(input("Enter an expense: "))
    userTotalExpenses += userExpense
    moreExpenses = input("Do you have more expenses? Enter Y for yes and any key for No: ")

print()
if userTotalExpenses > userBudget:
    print("You are over your budget of", userBudget, "by ", "$", (userTotalExpenses - userBudget))
elif userBudget > userTotalExpenses:
    print("You were under your budget", userBudget, "by", "$", (userBudget-userTotalExpenses))
else:
    print("You used exactly your budget of", userBudget)



