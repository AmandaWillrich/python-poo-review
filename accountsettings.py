def create_account(accountnumber, owner, balance, limit):
    account = {'number': accountnumber,
               'owner': owner,
               'balance': balance,
               'limit': limit}
    return account

def deposit(accountnumber, amount):
    pass