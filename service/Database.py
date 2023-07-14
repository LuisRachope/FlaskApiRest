import json
import service.FolderLib as FolderLib

class Database:
    def __init__(self):
        serviceFolder = FolderLib.FindMyFolder()
        self.pathFile = f"{serviceFolder.getPathFolder()}/data/base.json"

        # Abrir o arquivo JSON
        with open(self.pathFile) as file:
            self.data = json.load(file)

    def ReadAll(self):
         # Retorna os dados do json como se fose da base
        return self.data 
    
    def ReadByName(self, userId):
        users = self.data['usuarios']
        user = ''

        for row in users:
            if row['id'] == userId:
               user = row
        
        return user
    
