from pathlib import Path

class FindMyFolder:
    def __init__(self):
        # Obter o diretório do arquivo atual
        self.diretorio_atual = Path(__file__).resolve().parent

    def getPathFolder(self):
        # Obtem e retorna o caminho até a pasta do projeto
        PathFolder = self.diretorio_atual.parent
        return PathFolder