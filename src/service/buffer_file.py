from io import BytesIO
import json

class BufferFile:
    def __init__(self):
        self.json_data = {
            "id": 1001,
            "name": "Testando o file",
            "age": 27,
            "email": "teste@email.com"
        }
        self.buffer_stream = None

    def create_buffer_stream(self):
        try:
            # Serialize o JSON para uma string
            json_str = json.dumps(self.json_data)
            
            # Crie um buffer de memória com o conteúdo serializado
            self.buffer_stream = BytesIO(json_str.encode())
            return self.buffer_stream
        
        except Exception as e:
           raise (f"Erro ao criar o buffer de memória: {str(e)}")