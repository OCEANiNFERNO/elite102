import sqlite3 
from bank_functions import BankAccount

account = BankAccount()


def main():
    connection = sqlite3.connect('banking_app.db')
    cursor = connection.cursor()

    
while True:
    #print login user
    login_choice = account.login_menu()
    
    #Choice to login
    if login_choice == "1":
        #if login is successful
        if account.login():
           #prints out the banking choice
           banking_choice = account.banking_menu()
           #if you wish to check your balance
           if banking_choice == '1':
               account.check_balance()
           elif banking_choice == '2':
                account.withdraw()
           elif banking_choice == "3":
               account.deposit()
           elif banking_choice == '4':
               account.edit_user()
               
    elif login_choice == "2":
        account.create_user()
        account.create_account()

    #This is option 3        
    else:
        break
        





if __name__ == "__main__":
    main()
