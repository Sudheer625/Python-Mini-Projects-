class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Account Balance Updated:", self.balance)

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient Balance. Cannot withdraw.")
        else:
            self.balance -= amount
            print("Withdrawal successful. Account Balance:", self.balance)

    def check_balance(self):
        print("Account Balance:", self.balance)


# Create a Bank object and perform operations
user = Bank('Sudheer', 18, 'Male')
user.show_details()
user.deposit(10000)
user.withdrawal(1000)
user.check_balance()