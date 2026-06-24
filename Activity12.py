actual_cost = float(input("Enter the number of buy amount: "))
sale_amount = float(input("Enter the number of sale amount: "))

if sale_amount > actual_cost:
    profit = sale_amount - actual_cost
    print("My profit is: ",profit)
else:
    Loss = actual_cost - sale_amount
    print("Loss is: ",Loss)