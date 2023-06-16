from flask import Flask, render_template, request, abort, redirect, url_for
import json, sys
# sys.path.insert(1, '/mnt/c/Users/isabe/Documents/Documentos/UFU/2022-1/ASA/trab1/src/ampq')
# import new_task
sys.path.insert(0, '/mnt/c/Users/isabe/Documents/Documentos/UFU/2022-1/ASA/trab1/src/ampq')
from new_task import Tasker

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST','GET'])
def menu():
    return render_template('index.html')

@app.route('/menuCadastro', methods=['POST','GET'])
def menuCadastro():
    return render_template('cadastro.html')

@app.route('/menuList', methods=['POST','GET'])
def menuList():
    return render_template('list.html')

@app.route('/menuActions', methods=['POST','GET'])
def menuActions():
    return render_template('buscaEstudante.html')

@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    if request.method == 'POST':
       json_estudante = json.dumps(request.form.to_dict())
       #mensageria
       task_insert = Tasker('student')
       task_insert.send('insert',json_estudante)

       return 'Estudante enviado para cadastro'
    else:
        abort(403) #status 403 = proibido

@app.route('/listar', methods=['POST','GET'])
def listar():
    if request.method == 'POST':
        # return request.form.to_dict()
        task_get = Tasker('student')
        task_get.send('get',json.dumps(request.form.to_dict()))
        return "objetos listados na fila"
       #colocar o serviço de mensageria para buscar o array de json
    else:
        abort(403) #status 403 = proibido

@app.route('/actions', methods=['POST','GET'])
def actions():
    if request.method == 'POST':
        return render_template('actions.html', matricula=request.form.to_dict()["matricula"])
        # return request.form.to_dict()["matricula"]
       #colocar o serviço de mensageria para buscar o array de json
    else:
        abort(403) #status 403 = proibido

@app.route('/delete', methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        return "usuario deletado"
        # return request.form.to_dict()["matricula"]
       #colocar o serviço de mensageria para buscar o array de json
    else:
        abort(403) #status 403 = proibido

if __name__ == '__main__':
    app.run(debug=True)