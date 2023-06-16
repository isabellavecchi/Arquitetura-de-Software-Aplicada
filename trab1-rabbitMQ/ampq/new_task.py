#!/usr/bin/env python
import pika
import sys

class Tasker:
    #constructor
    def __init__(self, task):
        #criando a conexao
        self.connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost') )
        self.channel = self.connection.channel()
        self.task = task
        self.routing_key = task

    def send(self, atividade, mensagem):
        #criando a fila de mensagens, que n se perde ao rabbitmq ser reiniciado
        self.channel.queue_declare(queue=self.task, durable = True)

        # message = ' '.join(sys.argv[1:]) or "Hello World"
        message = atividade + '#' + mensagem or "Nenhum dado enviado"

        #especificando para qual fila mandar
        self.channel.basic_publish(  exchange = '',
                                routing_key = self.routing_key,
                                # se eu adicionar # = n caracteres, * = 1 palavra
                                body = message,
                                # mecanismo também para a msg n se perder ao rabbitmq ser reiniciado
                                properties=pika.BasicProperties(
                                    delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
                                )
                            )
        print(" [x] Sent %r" % message)

        self.connection.close()