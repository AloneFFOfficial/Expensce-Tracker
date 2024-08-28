import sqlite3

class Database:
    def connect(func):
        def wrapper(self, *args, **kwargs):
            print(f"Connecting to the database...")
            con = sqlite3.connect("expense.db")
            cur = con.cursor()
            result = func(self, cur, *args, **kwargs)
            con.commit()
            con.close()
            print(f"Database connection closed.")
            return result
        return wrapper

    @connect  
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
        tables = cur.fetchall()
        for table in tables:
            if table[0] == table_name:
                return True
                
        print("Table not found")
        print("Creating new table")
        return self.create_table(table_name)

    @connect
    def get_data(self, cur, table_name):
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        column_names = [description[0] for description in cur.description]
        data = [dict(zip(column_names, row)) for row in rows]
        return data



    @connect
    def aad_data(self, cur, table_name, data):
    # Assuming 'data' is a tuple or list of individual values
        cur.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)", data)
        return "Data added Successfully"
