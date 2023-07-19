from ..service.database import Database

class UserRepository(Database):
    def __init__(self) -> None:
        super().__init__()