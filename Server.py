from flask import Flask
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('registerUser')
def register_user(user):
    arquivo = open("Dados.txt", "a+")
    json_user = json.dumps(user)
    arquivo.write("\n" + json_user)
    arquivo.close()
    socketio.emit("registerUser", user)


@socketio.on('getUsers')
def get_users():
    arquivo = open("Dados.txt", "r+")
    linhas = arquivo.readlines()
    users = []
    for linha in linhas:
        if linha == "\n":
            continue
        else:
            user = json.loads(linha)
            users.append(user)
    socketio.emit("getUsers", users)


'''@socketio.on('autenticateUser')
def auntenticate_user(user_receive):
    arquivo = open("Dados.txt", "r+")
    linhas = arquivo.readlines()
    for linha in linhas:
        if linha == "\n":
            continue
        else:
            user = json.loads(linha)
            if user_receive['nome'] == user['nome']:
                if user_receive['senha'] == user['senha']:
                    socketio.emit("autenticateUser", True)
                    break'''


if __name__ == '__main__':
    socketio.run(app)