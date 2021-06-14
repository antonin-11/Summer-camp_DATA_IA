
def show_transactions(transactions):
    for transaction in transactions:
        if (transaction > 0):
            print(f"You received {transaction} euros")
        else:
            print(f"You spent {transaction} euros")

transactions = [512, 42.08, -12]
show_transactions(transactions)