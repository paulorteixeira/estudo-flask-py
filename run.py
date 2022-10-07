from flask import Flask, jsonify, request
import json

desenvolvedor = ['asdad','123123']

app = Flask(__name__)

@app.route("/<int:numero>",methods=['GET'])
def ola(numero):
    return 'Olá mundo! {}'.format(numero)

@app.route("/",methods=['GET'])
def pessoa():
    return jsonify({'nome':'Paulo'})

@app.route("/soma",methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'SOMA':total})



@app.route("/dev/<int:id>/",methods=['GET','POST'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            print('asdasdasd')
            print(id,desenvolvedor[id])
            response = desenvolvedor[id]
        except IndexError:
            mensagem = 'Desenvolvedor não existe'
            response = {'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro não previsto'
            response = {'mensagem':mensagem}
    return jsonify(response)

if __name__ == "__main__":
    app.run()
