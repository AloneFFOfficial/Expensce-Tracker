from database import Database
class Main:
  table_name ="expenses"
  if __name__ == "__main__":
    db = Database()
    '''table_exists = db.check_table('expenses')
    if table_exists:
      print("Table exists!")
    else:
      print("Table was created.")
    table_name = input('Enter table name: ')
    n = int(input('Enter number of data: '))
    for i in range(n):
      data = input('Enter data: ').split()
      db.aad_data(table_name,data)'''

    print(db.get_data(f"{table_name}"))