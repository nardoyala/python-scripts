import os
import pyperclip

def run():
    ACCOUNTS_PATH = os.getcwd() + "\\bankAccountInfo\\accounts"
    ACCOUNTS = os.listdir(ACCOUNTS_PATH)
    options = list()
    
    for account in ACCOUNTS:
        if account.endswith(".txt"):
            options.append(account)
            bank_name = os.path.splitext(account)[0]
            print(str(options.index(account) + 1) + " " + bank_name)

    user_option = int(input("Please, pick an option: ")) - 1

    while user_option < 0 or user_option >= len(options):
        user_option = int(input("Please, pick proper option: ")) - 1

    with open(ACCOUNTS_PATH + "\\" + options[user_option], "r", encoding='utf-8') as file:
        bank_account = file.read()
        pyperclip.copy(bank_account)

    print("Account information copied")

if __name__ == '__main__':
    run()
