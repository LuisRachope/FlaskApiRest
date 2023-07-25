from service.database_service import DatabaseService

class UserRepository(DatabaseService):
    def __init__(self) -> None:
        super().__init__()