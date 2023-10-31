
import os
import sqlite3
from typing import Any

DATABASE = "src/data/db_generic.db"

class DatabaseRepository:
    def __init__(self):
        self.conn = None
        self.database = "src/data/db_generic.db"

    def connect_db(self) -> sqlite3:
        """Cria uma conexão com o banco de dados sqlite3

        Returns:
            sqlite3: Retorna a conexão com o banco de dados
        """
        if os.path.exists(self.database):
            self.conn = sqlite3.connect(self.database)
        else:
            self.conn = sqlite3.connect(self.database)

        return self.conn
        
    def close_connection(self) -> None:
        """Finaliza a sessão com o banco de dados
        """
        if self.conn is not None:
            self.conn.close()

    def create_table(self, table_name:str) -> None:
        """Realiza a criação da tabela de usuários (MOOK)

        Args:
            table_name (str): Nome que deseja dar para a tabela
        """

        query = str(
            f"""CREATE TABLE {table_name}
         (id INT PRIMARY KEY     NOT NULL,
         name           TEXT    NOT NULL,
         age            INT     NOT NULL,
         email          CHAR(50));"""
        )

        self.conn.execute(query)
        self.conn.commit()
        

    def insert_table(self, table_name: str) -> None:
        """Realiza um insert na tabela com o parametro 'table_name' (MOOK)

         Args:
            table_name (str): Nome que deseja dar para a tabela
        """
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

    def select_table(self, table_name: str) -> Any:
        """Realiza uma consulta no banco de dados para a tabela a qual deseja com o parametro 'table_name'

        Args:
            table_name (str): Nome que deseja dar para a tabela

        Returns:
            any: _description_
        """
        data = self.conn.execute(f"SELECT * FROM {table_name}")
        print(data.fetchall())
        return data

    def execute(self, query: str, params=None) -> None:
        """Executa a query no banco de dados

        Args:
            query (string): Representa a consulta que será realizada em forma de string
            params (tupla, optional): Representa os parametros de uma consulta, podendo ser mais de um. Default is none.
        """

        if not self.conn:
            self.conn = self.connect_db()
        with self.conn:
            if params:
                self.conn.execute(query, params)
            else:
                self.conn.execute(query)

    def fetch_one(self, query, params=None) -> Any:
        """fetch_one retorna apenas um resultado da lista

        Args:
            query (string): Representa a consulta que será realizada em forma de string
            params (tupla, optional): Representa os parametros de uma consulta, podendo ser mais de um. Default is none.
        """
        if not self.conn:
            self.conn = self.connect_db()
        with self.conn:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchone()

    def fetch_all(self, query, params=None) -> Any:
        """fetch_one retorna uma lista de resultados

        Args:
            query (string): Representa a consulta que será realizada em forma de string
            params (tupla, optional): Representa os parametros de uma consulta, podendo ser mais de um. Default is none.
        """
        if not self.conn:
            self.conn = self.connect_db()
        with self.conn:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()

    def insert_db(self, table: str, params: str, payload):
        """Realiza um insert generico no banco de dados

        Args:
            table (string): Nome da tabela que será realizado o insert
            params (string): Conjunto de colunas que irão ser informadas para o insert na tabela
            values (obj): Dados que serão inseridos

            Exemplo: rows = ({"id": 99, "name": "teste1", "age": 55, "email": "teste@email.com"},)
        """

        if not self.conn:
            self.conn = self.connect_db()
        with self.conn:
            # Instancia a conexão com o banco de dados
            cursor = self.conn.cursor()

            values = []
            # Use um loop para adicionar os valores ao dicionário com chaves geradas automaticamente
            for i, value in enumerate(payload):
                values.append(value[1])

            # Construa a consulta SQL com base nos dados
            consulta_sql = f"INSERT INTO {table} ({', '.join(params)}) VALUES ({', '.join(['?']*len(values))})"

            # Execute a consulta SQL com os valores
            return cursor.execute(consulta_sql, values)
        
        