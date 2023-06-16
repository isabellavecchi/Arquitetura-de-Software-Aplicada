import pika, sys, os, json
sys.path.insert(1, '/mnt/c/Users/isabe/Documents/Documentos/UFU/2022-1/ASA/trab1/src/flask_app')
from connectDB import ConectaBD
from studentDAO import EstudanteDAO
from student import Estudante

class Worker():

    #constructor
    def __init__(self,name_task):
        self.task = name_task
        # criando a conexao
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost') )
        self.channel = connection.channel()

    def main(self):
        # criando a fila de mensagens, que n se perde ao rabbitmq ser reiniciado
        #como não sabemos qual programa rodará primeiro,
        #é boa pratica declarar a fila 2x.
        self.channel.queue_declare(queue=self.task, durable = True)
        print(' [*] Waiting for messages. To exit press CTRL+C')

        # subscribing a callback function to a queue
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body.decode())
            # conexao = ConectaBD()
            # estudanteDAO = EstudanteDAO(conexao)
            # estudanteDAO.addEstudanteJson(json_estudante)
            # se der um Ctrl C antes da msg ser enviada, ele espera
            ch.basic_ack(delivery_tag = method.delivery_tag)
            self.metodo(body.decode())
            print(" [x] Done")

        # para conectar apenas um usuario por vez
        self.channel.basic_qos(prefetch_count=1)

        # amarrando a callback aa queue desejada
        self.channel.basic_consume(  queue = self.task,
                                # auto_ack = True,
                                on_message_callback = callback)

        # entrando num loop infinito para receber mensagens
        self.channel.start_consuming()
    
    def consume(self):
        try:
            self.main()
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def metodo(self,message):
        try:
            message = message.split('#')
            action = message[0]
            json_args = json.loads(message[1])
            if(action == 'insert'):
                self.insert(json_args)
            elif(action == 'get'):
                self.get(json_args)
            elif(action == 'update'):
                self.update(json_args)
            elif(action == 'delete'):
                self.delete(json_args)
            conexao = ConectaBD()
            estudanteDAO = EstudanteDAO(conexao)
            print(message[1])
            estudanteDAO.addEstudanteJson(json_args)
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def insert(self,json_estudante):
        try:
            conexao = ConectaBD()
            estudanteDAO = EstudanteDAO(conexao)
            print(json_estudante)
            estudanteDAO.addEstudanteJson(json_estudante)
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def get(self,json_args):
        try:
            conexao = ConectaBD()
            estudanteDAO = EstudanteDAO(conexao)
            print(json_args)
            if(json_args['rbOrder']=="rbMatricula"):
                estudantes = estudanteDAO.getStudentsByNameOrderedRegister(json_args['nome'])
                for estudante in estudantes:
                    estudante.printa()
            elif(json_args['rbOrder']=="rbNome"):
                estudantes = estudanteDAO.getStudentsByNameOrderedName(json_args['nome'])
                for estudante in estudantes:
                    estudante.printa()
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)