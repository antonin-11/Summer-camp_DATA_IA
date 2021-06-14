import json

class Budget:
    _transactions = {}

    def new_transaction(cls, category, value):
        try:
            Budget._transactions[category].append(int(value))
        except:
            Budget._transactions[category] = [int(value)]

    def get_category(cls):
        category = []
        for cate in Budget._transactions:
            category.append(cate)
        return(category)

    def show_transactions(cls, category):
        for value in Budget._transactions[category]:
            print(value)

    def show_all_transactions(cls):
        for category in Budget._transactions:
            print(category)
            for value in Budget._transactions[category]:
                print(value)
            print("")
    
    def my_balance(csl):
        tt_value = 0
        for category in Budget._transactions:
            for value in Budget._transactions[category]:
                tt_value += value
        print("\nmy balance is", tt_value, "\n")

def print_menu():
    print("Choose between :")
    print("1 - consult my balance")
    print("2 - add a new transaction")
    print("3 - consult your transactions history")
    print("4 - quit")

def add_new_transaction():
    value = 0
    category = ""

    print("")
    print("what is the value of your transaction : ", end='')
    value = input()
    while (value.isdigit() == False):
        print("what is the value of your transaction : ", end='')
        value = input()
    print("what is the category of your transaction : ", end='')
    category = input()
    while (category.isalpha() == False):
        print("what is the category of your transaction : ", end='')
        category = input()
    wallet.new_transaction(category, value)
    print("")

line = ""
wallet = Budget()

while (line != "4"):
    print_menu()
    line = input()
    if (line.isdigit() and int(line) >= 1 and int(line) <= 4):
        if (int(line) == 1):
            wallet.my_balance()
        if (int(line) == 2):
            add_new_transaction()
        if (int(line) == 3):
            print("")
            wallet.show_all_transactions()
    else:
        print("Error ", end='')
    