import src.data.database as db


class DatabaseRepository:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = db.get_connection()
        return self.conn

    def execute(self, query:str, params=None):
        """_summary_

        Args:
            query (string): Representa a consulta que será realizada em forma de string
            params (tupla, optional): Representa os parametros de uma consulta, podendo ser mais de um. Default is none.
        """

        if not self.conn:
            self.connect()
        with self.conn:
            if params:
                self.conn.execute(query, params)
            else:
                self.conn.execute(query)
 
    def fetch_one(self, query, params=None):
            """fetch_one retorna apenas um resultado da lista

            Args:
                query (string): Representa a consulta que será realizada em forma de string
                params (tupla, optional): Representa os parametros de uma consulta, podendo ser mais de um. Default is none.
            """
            if not self.conn:
                self.connect()
            with self.conn:
                cursor = self.conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchone()

    def fetch_all(self, query, params=None):
            """fetch_one retorna uma lista de resultados

            Args:
                query (string): Representa a consulta que será realizada em forma de string
                params (tupla, optional): Representa os parametros de uma consulta, podendo ser mais de um. Default is none.
            """
            if not self.conn:
                self.connect()
            with self.conn:
                cursor = self.conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
