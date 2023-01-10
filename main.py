from accountsettings import Account

# Amandas_account = create_account(123, 'Amanda', 400, 1000)
# print(Amandas_account)

# deposit(Amandas_account, 100)
# show_balance(Amandas_account)

# withdraw(Amandas_account, 50)
# show_balance(Amandas_account)

account1 = Account(123, 'Amanda', 1000, 2000)
account2 = Account(321, 'Cris', 1000, 5000)

account1.transfer(200, account2)
account2.show_balance()

print(account1.balance)

account1.withdraw(300)
account1.show_balance()

account1.withdraw(3000)
account1.show_balance()
