# def create_account(accountnumber, owner, balance, limit):
#     account = {'accountnumber': accountnumber,
#                'owner': owner,
#                'balance': balance,
#                'limit': limit}
#     return account


# def deposit(account, amount):
#     account['balance'] += amount


# def withdraw(account, amount):
#     account['balance'] -= amount


# def show_balance(account):
#     print(f"Your current balance is R$ {account['balance']}")

class Account():
    def __init__(self, account_number, owner, balance, limit):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def show_balance(self):
        print(f'The account owned by {self.__owner}',
              f'has the balance of R$ {self.__balance}')

    def deposit(self, amount):
        self.__balance += amount

    def __can_withdraw(self, target_amount):
        available_money = (self.__balance + self.__limit)
        return target_amount <= available_money

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.__balance -= amount
        else:
            print('The amount exceeds the limit')

    def transfer(self, amount, target):
        self.withdraw(amount)
        target.deposit(amount)

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @limit.setter
    def limit(self, limit):
        self.__limit = limit
