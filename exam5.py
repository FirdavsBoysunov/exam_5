import psycopg2
import threading
import time
# =============================== masala 1
conn = psycopg2.connect(database = 'new_db', 
                        user = 'postgres', 
                        host = 'localhost',
                        password = '112',
                        port = 5432
                        )


def func_connect_db():

    cur = conn.cursor()
    create_table = '''CREATE TABLE product(
                id SERIAL PRIMARY KEY,
                name VARCHAR(300) NOT NULL,
                price float,
                color VARCHAR(300),
                image VARCHAR(500)
        );'''

    cur.execute(create_table)
    conn.commit()

# func_connect_db()



# =====================================> masala 2


class Crud:
    def __init__(self, conn):
        self.conn = conn
    
    def __enter__(self):
        self.cur = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
    
    @staticmethod
    def insert():
        insert_into = '''INSERT INTO product(name, price, color, image)
                         VALUES('not 5', 100, 'green', 'http://sdfldjfd'),
                               ('not 7', 200, 'green', 'http://sdfsdfhll');'''
        return insert_into

    @staticmethod
    def select_all():
        select_from = '''SELECT * FROM product;'''
        return select_from

    @staticmethod
    def update_product():
        update_prot = '''UPDATE product SET name='updated_name', price=150
                         WHERE id > 5;'''
        return update_prot
    @staticmethod
    def delete():
        delete_prot = '''DELETE FROM product
                            WHERE id = %s;'''


        return delete_prot
def main():
    try:
        conn = psycopg2.connect(database="new_db", user="postgres", password="112", host="localhost", port=5432)
        with Crud(conn) as crud:
            while True:
                choice = input('add data => 1\nget all products => 2\nupdate table => 3\ndelete data => 4\nexit => q\n....: ')
                if choice == '1':
                    table = Crud.insert()
                    crud.cur.execute(table)
                    crud.conn.commit()
                    print('Added data')
                elif choice == '2':
                    select_query = Crud.select_all()
                    crud.cur.execute(select_query)
                    products = crud.cur.fetchall()
                    for product in products:
                        print(product)
                elif choice == '3':
                    update_query = Crud.update_product()
                    crud.cur.execute(update_query)
                    crud.conn.commit()
                    print('Updated data')
                elif choice == '4':
                    delete = Crud.delete()
                    data = input('enter id: ')
                    crud.cur.execute(delete, data)
                elif choice == 'q':
                    print('Exiting...')
                    break
 
    except Exception:
        print('error')

# main()  





# =============================================== masala 3
class Alphabet:
    def __init__(self):
        self.letters = [chr(i) for i in range(65, 91)] 
        self.index = 0


    def __iter__(self):
        return self
    

    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration

# alphabet = Alphabet()
# for letter in alphabet:
#     print(letter)

        
# # =============================================== masala 4

# def print_numbers():
#     x = input('enter number')
#     for number in range(1, x+1):
#         print(number)
#         time.sleep(1)

# def print_letters():
#     for letter in "ABCDEFG":
#         print(letter)
#         time.sleep(1)


# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# =============================================== masala 5

# =============================================== masala 6
conne = {
    'database': 'n48group',
    'user': 'postgres',
    'host': 'localhost',
    'password': '112',
    'port': 5432
}

class DBconnect:
    def __init__(self):
        self.connect = psycopg2.connect(**conne)

    def __enter__(self):
        self.cur = self.connect.cursor()
        return self.connect, self.cur
    @staticmethod
    def create_table():
        create = '''create table new_praject(
            id serial primary key,
            name varchar(200)
        );'''
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()
        if self.connect:
            self.connect.close()



product = DBconnect

# with product as (conn, cur):
#     table = DBconnect.create_table()
#     cur.execute(table)
#     conn.commit()
#     print("created table")
    
# =============================================== masala 7

# =============================================== masala 8







