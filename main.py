from accountsettings import create_account, deposit, show_balance, withdraw

Amandas_account = create_account(123, 'Amanda', 400, 1000)
print(Amandas_account)

deposit(Amandas_account, 100)
show_balance(Amandas_account)

withdraw(Amandas_account, 50)
show_balance(Amandas_account)
