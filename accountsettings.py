def create_account(accountnumber, owner, balance, limit):
    account = {'accountnumber': accountnumber,
               'owner': owner,
               'balance': balance,
               'limit': limit}
    return account


def deposit(account, amount):
    account['balance'] += amount


def withdraw(account, amount):
    account['balance'] -= amount


def show_balance(account):
    print(f"Your current balance is R$ {account['balance']}")
