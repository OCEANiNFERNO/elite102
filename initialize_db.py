import sqlite3

DB_NAME = 'banking_app.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # This is the account table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user
            (pin integer primary key, 
            username text, 
            password text,
            address text,
            email text,
            phone_number integer
            )
    ''')

        # This is the user table
    print("Creating second table")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS account                   
            (id integer primary key, 
            user_id integer,
            authorization text,
            balance integer,
            FOREIGN KEY (user_id) REFERENCES user(pin)
            )           
    ''')


    print("Table created.")

    # # Insert data into
    # print("Inserting sample data...")
    # cursor.execute('''
    #     INSERT INTO account (name, age,grade, gpa) VALUES
    #     ('Alice', 16, '10th', 3.5),
    #     ('Bob', 17, '11th', 3.8),
    #     ('Charlie', 15, '9th', 3.2)
    # ''')
    # print("Sample data inserted.")
    # # Commit the changes and close the connection
    # print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


initialize_database()
