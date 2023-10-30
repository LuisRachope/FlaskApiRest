import os
import sqlite3


class Database:
    def __init__(self):
        self.conn = ""
        self.database = "src/data/db_generic.db"

    def connect_db(self):
        if os.path.exists(self.database):
            self.conn = sqlite3.connect(self.database)
            return self.conn
        else:
            self.conn = sqlite3.connect(self.database)
            return None

    def create_table(self, table_name):
        query = str(
            f"""CREATE TABLE {table_name}
         (id INT PRIMARY KEY     NOT NULL,
         name           TEXT    NOT NULL,
         age            INT     NOT NULL,
         email          CHAR(50));"""
        )

        self.conn.execute(query)
        self.conn.commit()

    def insert_table(self, table_name):
        self.conn.execute(f"INSERT INTO {table_name} (id,name,age,email) VALUES (1, 'Paul', 28, 'paul@email.com')")
        self.conn.execute(f"INSERT INTO {table_name} (id,name,age,email) VALUES (2, 'Mark', 31, 'mark@email.com')")
        self.conn.execute(f"INSERT INTO {table_name} (id,name,age,email) VALUES (3, 'Julia', 24, 'julia@email.com')")
        self.conn.execute(f"INSERT INTO {table_name} (id,name,age,email) VALUES (4, 'Nathan', 48, 'nathan@email.com')")
        self.conn.execute(f"INSERT INTO {table_name} (id,name,age,email) VALUES (5, 'Agatha', 19, 'agatha@email.com')")
        self.conn.execute(
            f"INSERT INTO {table_name} (id,name,age,email) VALUES (6, 'Maxwell', 62, 'maxwell@email.com')"
        )
        self.conn.execute(f"INSERT INTO {table_name} (id,name,age,email) VALUES (7, 'Jonh', 31, 'jonh@email.com')")
        self.conn.execute(
            f"INSERT INTO {table_name} (id,name,age,email) VALUES (8, 'Yennifer', 40, 'yennifer@email.com')"
        )
        self.conn.commit()

    def select_table(self, table_name):
        data = self.conn.execute(f"SELECT * FROM {table_name}")
        print(data.fetchall())
        return data
