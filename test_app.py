import requests
import json

def teste_enviar_json():

    json_body = {
        "mensagem": "qual a boa"
    }

    response = requests.post(
        "https://wilzt9a9qb.execute-api.us-east-1.amazonaws.com/default/ponderadaSemana2",
        data=json.dumps(json_body),
        headers={"senha": "pk", "Content-Type": "application/json"}
    )

    assert response.status_code == 200

    json_response = response.json()
    assert json_response == json_body

def teste_segurança():

    json_body = {
        "mensagem": "qual a boa"
    }

    response = requests.post(
        "https://wilzt9a9qb.execute-api.us-east-1.amazonaws.com/default/ponderadaSemana2",
        data=json.dumps(json_body),
        headers={"senha": "senha_incorreta", "Content-Type": "application/json"}
    )

    assert response.status_code == 401
    
def teste_tipo_request():

    response = requests.get("https://wilzt9a9qb.execute-api.us-east-1.amazonaws.com/default/ponderadaSemana2")

    assert response.status_code == 405

