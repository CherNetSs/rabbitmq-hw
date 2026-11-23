import time

from connection import connect

host, connection = connect()
try:
    channel = connection.channel()
    channel.queue_declare(queue="hello", durable=True, passive=True)
    for attempt in range(10):
        method, _, body = channel.basic_get(queue="hello")
        if method:
            channel.basic_ack(method.delivery_tag)
            print(f"[{host}] Received from hello: {body.decode()}")
            break
        time.sleep(1)
    else:
        raise SystemExit(f"[{host}] No messages in hello")
finally:
    connection.close()
