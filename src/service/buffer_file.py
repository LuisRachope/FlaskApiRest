from io import BytesIO
import json

# Intancia o buffer IO
buffer = BytesIO()

def create_buffer_stream(file_data: dict) -> BytesIO:
    """Cria um buffer do arquivo recebido pela variável file_data.

    Args:
        file_data (dict): Conteúdo que será transformado no buffer (arquivo temporário em memoria).

    Returns:
        BytesIO: Retorna o arquivo em buffer.
    """
    try:
        # Serialize o JSON para uma string
        json_str = json.dumps(file_data, indent=2).encode('utf-8')

        # Adiciona no buffer o conteúdo do arquivo
        buffer.write(json_str)

        # Retorna para o inicio do buffer
        buffer.seek(0)

        return buffer
    
    except Exception as e:
        raise Exception(f"Erro ao criar o buffer de memória: {str(e)}")