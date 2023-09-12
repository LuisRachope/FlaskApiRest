from src.repository import DatabaseRepository

table = 'user'
params = ':id, :name, :age, :email'

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
        """_summary_

        Args:
            id (integer): identificação do usuário no banco de dados

        Returns:
            _type_: retorna a linha do banco com as informações do usuário
        """
        response = self.insert_db(table, params, user)
        return response

