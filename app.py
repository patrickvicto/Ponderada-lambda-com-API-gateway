from flask import Flask, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'pk'
app.config['BASIC_AUTH_PASSWORD'] = 'pk'
basic_auth = BasicAuth(app)

@app.route('/', methods=['GET'])
def pagina_inicial():
    return "Se autentique e digite /mensagem para obter a mensagem, a senha esta no readme"

@app.route('/mensagem', methods=['GET'])
@basic_auth.required
def obter_mensagem():
    mensagem = {"mensagem": "Qual a boa?"}
    return jsonify(mensagem)

if __name__ == '__main__':
    app.run(debug=True)
