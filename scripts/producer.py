import pika

from connection import connect

host, connection = connect()
try:
    channel = connection.channel()
    channel.queue_declare(queue="hello", durable=True)
    channel.confirm_delivery()
    body = b"Hello World!"
    channel.basic_publish(
        exchange="", routing_key="hello", body=body,
        properties=pika.BasicProperties(delivery_mode=2),
        mandatory=True,
    )
    print(f"[{host}] Published to hello: {body.decode()}")
finally:
    connection.close()
