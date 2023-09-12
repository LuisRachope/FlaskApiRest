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
    
    def json_query(self, json):
        columns = ''
        values = ''
        for value in json.keys():
            columns += f"{value},"
            values += "?,"
            columns = columns[:-1]
            values = values[:-1]
        return columns, values
        
    def insert_db(self, table:str, params:str, values):
        """Insert no banco

            Args:
                table (string): Nome da tabela que será realizado o insert
                params (string): Conjunto de colunas que irão ser informadas para o insert na tabela
                values (obj): Dados que serão inseridos 

                Exemplo: rows = ({"id": 99, "name": "teste1", "age": 55, "email": "teste@email.com"},)
        """
        teste_params = params.replace(":", "")
        
        if not self.conn:
                self.connect()
        with self.conn:
            cursor = self.conn.cursor()
            cursor.executemany(f"INSERT INTO {table} ({teste_params}) VALUES({params})", values)
            return cursor.fetchall()        

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
        
        """
            Estudar com calma a questão do objeto
            class ObjetoPersonalizado:
                def __init__(self, **kwargs):
                    for key, value in kwargs.items():
                setattr(self, key, value)
                    meu_objeto = ObjetoPersonalizado(**meu_dict)
        """
