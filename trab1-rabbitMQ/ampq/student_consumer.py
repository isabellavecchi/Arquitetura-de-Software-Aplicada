''' import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch,method, properties, body):
    print(f"Serviço de Alunos - recebeu uma nova mensagem: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='studentsonly')

channel.basic_consume(queue=queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)

print("Começou a consumir...")

channel.start_consuming() '''

#!/usr/bin/env python
from worker import Worker
import sys, os

workerInsert = Worker('student')

workerInsert.consume()