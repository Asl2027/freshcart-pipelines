import pika
import sys
import json

name = sys.argv[1]
pattern = sys.argv[2]

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.exchange_declare(
    exchange='rapido-dispatch',
    exchange_type='topic'
)

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(
    exchange='rapido-dispatch',
    queue=queue_name,
    routing_key=pattern
)

print(f"{name} listening for: {pattern}", flush=True)

def callback(ch, method, properties, body):
    message = json.loads(body)

    if not message.get('zone'):
        print(f"{name} rejected bad message: {message}", flush=True)
        ch.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=False
        )
    else:
        print(f"{name} received: {message}", flush=True)
        ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback
)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print(f"{name} stopped.", flush=True)
    channel.stop_consuming()
finally:
    connection.close()
