import json

class VerificadorTipo:
    @staticmethod
    def verificar_tipo(event):
        if event['httpMethod'] == 'POST':
            return 1
        else:
            return 0

class VerificadorAcesso:
    @staticmethod
    def verificar_senha(event):
        senha_correta = "pk"
        if 'senha' in event['headers'] and event['headers']['senha'] == senha_correta:
            return 1
        return 0

def lambda_handler(event, context):
    verificador = VerificadorTipo()
    tipo_requisicao = verificador.verificar_tipo(event)
    verificador_acesso = VerificadorAcesso()
    permissao = verificador_acesso.verificar_senha(event)

    if tipo_requisicao == 1:
        if permissao == 1:
            body = json.loads(event['body'])
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps(body)
            }
        else:
            return {
                'statusCode': 401,
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'error': 'Acesso negado,insira a senha_correta'})
            }
    else:
        return {
            'statusCode': 405,
            'headers': {
                'Allow': 'POST'
            },
            'body': json.dumps({'error': 'Metodo nao permitido,Por favor envie um json pelo metodo post'})
        }
