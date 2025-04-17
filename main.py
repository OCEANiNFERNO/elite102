import sqlite3
from initialize_db import initialize_database
initialize_database()

from bank_functions import BankAccount

account = BankAccount()



def main():

    while True:
        #print login user
        login_choice = account.login_menu()

        if login_choice == "1":
            account.login()
            #call login function
            #elif login_choice == "2":
                #call choi
            #elif login_choice == "3":

        #bank_chopice == account.banking_menu():
           # pass
            # if statements for all the choices.
        # say user wants to login, prompt bank app login

        #login
        #create account

        #




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
