import json
from service.folder_service import FolderService

class DatabaseService(FolderService):
    def __init__(self):
        super().__init__()
        self.path_file = f"{self.get_path_folder()}/data/base.json"

        # Abrir o arquivo JSON
        with open(self.path_file) as file:
            self.data = json.load(file)

    def read_all(self):
         # Retorna os dados do json como se fose da base
        return self.data 
    
    def read_by_id(self, user_id):
        users = self.data['usuarios']
        user = ''

        for row in users:
            if row['id'] == user_id:
               user = row
        
        return user
    
