import sqlite3 
from bank_functions import BankAccount

account = BankAccount()


def main():
    connection = sqlite3.connect('banking_app.db')
    cursor = connection.cursor()

    
while True:
        #print login user
    login_choice = account.login_menu()

    if login_choice == "1":
        if account.login():
           banking_choice = account.banking_menu()
           if banking_choice == '1':
               account.check_balance()
                
    elif login_choice == "2":
        account.create_user()
        account.create_account()
            #elif login_choice == "3":
    else:
        break
        




#     connection = sqlite3.connect('example.db')
#     cursor = connection.cursor()

#     # Get all rows from the students table
#     print("Fetching all rows from the account table...")
#     results = cursor.execute('''
#         SELECT * FROM account
#     ''')

#     print("Results:")
#     for row in results:
#         print(row)

#     # Get all students with a GPA greater than 3.5
#     print("Fetching students with GPA greater than 3.5...")
#     results = cursor.execute('''
#         SELECT * FROM students WHERE gpa > 3.5
#     ''')
#     print("Results:")
#     for row in results:
#         print(row)

#     connection.close()


if __name__ == "__main__":
    main()
