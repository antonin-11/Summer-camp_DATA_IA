
class Budget:
    _transactions = []

    def add_transactions(cls, new_transactions):
        for transaction in new_transactions:
            Budget._transactions.append(transaction)
    
    def show_transactions(cls):
        for transaction in Budget._transactions:
            if (transaction > 0):
                print(f"You received {transaction} euros")
            else:
                print(f"You spent {transaction} euros")


transactions = [512, 42.08, -12]

wallet = Budget()
wallet.add_transactions(transactions)
wallet.show_transactions()