import sqlite3

class Database:
    def connect(func):
        def wrapper(self, *args, **kwargs):  # Include self to access instance
            con = sqlite3.connect("expense.db")
            cur = con.cursor()
            result = func(self, cur, *args, **kwargs)  # Pass self and cursor to the function
            con.commit()
            con.close()  # Close connection
            return result
        return wrapper

    @connect  # No need for @staticmethod
    def create_table(self, cur, table_name):
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                Date TEXT,
                Time TEXT,
                Amount REAL,
                Product TEXT,
                Description TEXT
            )
        """)
        return "Table Created"

    @connect
    def check_table(self, cur, table_name):
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cur.fetchall()  # Fetch all results
        for table in tables:
            if table[0] == table_name:
                return True  # Table found

        # If table is not found, create it
        print("Table not found")
        print("Creating new table")
        return self.create_table(table_name)  # Use self to call the instance method

