class Bank:
    def __init__(self, balance: float):
        self.balance = balance

    def add(self, income: float):
        self.balance += income
        print(f"{income} qo'shildi. Jami balans: {self.balance}")

    def withdraw(self, outcome: float):
        if outcome > self.balance:
            print("no money get out here")
        else:
            self.balance -= outcome
            print(f"{outcome} yechib olindi. Jami balans: {self.balance}")

    def show_balance(self):
        print(f"Jami balans: {self.balance}")

bank = Bank(1000.0)
bank.add(500.0)
bank.withdraw(200.0)
bank.show_balance()

