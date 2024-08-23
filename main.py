from database import Database
class Main:
  if __name__ == "__main__":
    db = Database()
    table_exists = db.check_table('expenses')
    if table_exists:
      print("Table exists!")
    else:
      print("Table was created.")
