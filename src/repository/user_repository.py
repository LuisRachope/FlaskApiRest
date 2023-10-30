from src.repository import DatabaseRepository

table = "user"
params = ":id, :name, :age, :email"
parametros = ["id", "name", "age", "email"]


class UserRepository(DatabaseRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_by_id(self, id: int):
        """Pesquisa no banco um usuário pelo Id

        Args:
            id (integer): identificação do usuário no banco de dados

        Returns:
            _type_: retorna a linha do banco com as informações do usuário
        """
        response = self.fetch_one(f"SELECT * FROM {table} WHERE id = {id}")
        return response

    def get_all(self):
        """Pesquisa todos usuários no banco

        Args:
            id (integer): identificação do usuário no banco de dados

        Returns:
            _type_: retorna a linha do banco com as informações do usuário
        """
        return self.fetch_all(f"SELECT * FROM {table}")

    def create_users(self, user):
        """Cria um novo usuário no banco de dados, baseando-se no payload
        Args:
            id (integer): identificação do usuário no banco de dados

        Returns:
            _type_: retorna a linha do banco com as informações do usuário
        """
        self.insert_db(table, parametros, user)
        response = self.get_by_id(user[0][1])
        return response
