from src.repository import DatabaseRepository

table = 'user'

class UserRepository(DatabaseRepository):
    def __init__(self) -> None:
        super().__init__()
    
    def get_by_id(self, id: int):
        """_summary_

        Args:
            id (integer): identificação do usuário no banco de dados

        Returns:
            _type_: retorna a linha do banco com as informações do usuário
        """
        response = self.fetch_one(f"SELECT * FROM {table} WHERE id = {id}")
        return response
    
    def get_all(self):
        """_summary_

        Args:
            id (integer): identificação do usuário no banco de dados

        Returns:
            _type_: retorna a linha do banco com as informações do usuário
        """
        response = self.fetch_all(f"SELECT * FROM {table}")
        return response
