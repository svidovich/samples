import os
import pika


RABBITMQ_HOST = os.environ['RABBITMQ_HOST']

rabbitmq_connection = None
rabbitmq_channel = None

def get_rabbitmq_connection():
    global rabbitmq_connection
    if rabbitmq_connection is None:
        connection_parameters = pika.ConnectionParameters(RABBITMQ_HOST)
        rabbitmq_connection = pika.BlockingConnection(connection_parameters)
    return rabbitmq_connection


def get_rabbitmq_channel():
    global rabbitmq_channel
    if rabbitmq_channel is None:
        rabbitmq_channel = get_rabbitmq_connection().channel()
    return rabbitmq_channel


def main():
    pass


if __name__ == '__main__':
    main()
