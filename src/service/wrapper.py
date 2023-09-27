import json

class ResponseWrapper:
    def generate_response(buffer, filename: str, content_type='application/octet-stream'):
        try:
            if buffer:
                # Volte para o início do buffer
                buffer.seek(0)

                # Leia os bytes do buffer
                buffer_content = buffer.read()

                # Converta os bytes para uma representação serializável (por exemplo, base64)
                serialized_content = buffer_content.hex()  # Use hex para representação hexadecimal

                # Configure os dados que você deseja incluir no JSON de resposta
                response_data = {
                    "filename": filename,
                    "content_type": content_type,
                    "content": serialized_content
                }

                # Converta os dados para uma string JSON
                response_json = json.dumps(response_data)

                return response_json
            else:
                print("Nenhum buffer de memória foi fornecido.")
                return None
        except Exception as e:
            print(f"Erro ao criar a resposta: {str(e)}")
            return None
