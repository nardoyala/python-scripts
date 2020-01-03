import os
import pyperclip

accountsPath = "D:\\proyectos\\python\\scripts\\bankAccount\\accounts"
accounts = os.listdir(accountsPath)
options = list()

for account in accounts:
    if account.endswith(".txt"):
        options.append(account)
        bankName = os.path.splitext(account)[0]
        print(str(options.index(account) + 1) + " " + bankName)

userOption = int(input("Please, pick an option: ")) - 1

while userOption < 0 or userOption >= len(options):
    userOption = int(input("Please, pick proper option: ")) - 1

with open(accountsPath + "\\" + options[userOption], "r", encoding='utf-8') as file:
    bankAccount = file.read()
    pyperclip.copy(bankAccount)

print("Account information copied")
