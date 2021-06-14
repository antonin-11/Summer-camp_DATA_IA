import json

class Budget:
    _transactions = {}

    def __init__(cls, patch):
        with open(patch) as f:
            field = json.load(f)
            for transaction in field["transactions"]:
                try:
                    Budget._transactions[transaction["category"]].append(transaction["value"])
                except:
                    Budget._transactions[transaction["category"]] = [transaction["value"]]

    def get_category(cls):
        category = []
        for cate in Budget._transactions:
            category.append(cate)
        return(category)

    def show_transactions(cls, category):
        for value in Budget._transactions[category]:
            print(value)

wallet = Budget("./data.json")
for category in wallet.get_category():
    print(category) 
    wallet.show_transactions(category)