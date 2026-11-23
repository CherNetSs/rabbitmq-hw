import argparse
import getpass
import os

import pika


def connect():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="IP RabbitMQ")
    options = parser.parse_args()
    password = os.environ.get("RABBITMQ_PASSWORD") or getpass.getpass("RabbitMQ password: ")
    credentials = pika.PlainCredentials(os.environ.get("RABBITMQ_USER", "netology"), password)
    return options.host, pika.BlockingConnection(
        pika.ConnectionParameters(options.host, credentials=credentials, socket_timeout=10)
    )
