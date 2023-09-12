from src.repository.user_repository import UserRepository
import json

class UserController(UserRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_user_by_id(self, user_id:int):
        """User get by id

        Args:
            user_id (string): Id de identificação do usuário no banco de dados

        Returns:
            _type_: Retorna a linha do usuário no banco de dados
        """
        return self.get_by_id(user_id)

    def get_users_all(self):
        """User all users 

        Returns:
            _type_: Retorna a lista de usuários no banco de dados
        """
        return self.get_all()
    
    def create_user(self, user):
        """Cria um usuário no banco

        Returns:
            _type_: Retorna a lista de usuários no banco de dados
        """
        user_tuple = tuple(user.items())

        return self.create_users(user_tuple)