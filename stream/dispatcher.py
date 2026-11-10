import pika
import json
import random
import time
from datetime import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.exchange_declare(
    exchange='rapido-dispatch',
    exchange_type='topic'
)

cities = {
    'bangalore': ['koramangala', 'indiranagar', 'whitefield'],
    'chennai': ['tnagar', 'velachery', 'adyar']
}

order_id = 1

print("Dispatcher started...", flush=True)

try:
    while True:
        city = random.choice(list(cities.keys()))
        zone = random.choice(cities[city])
        order_type = random.choice(['ride', 'food'])

        routing_key = f"{city}.{zone}.{order_type}"

        message = {
            "id": order_id,
            "city": city,
            "type": order_type,
            "ts": datetime.now().isoformat()
        }

        if order_id % 10 != 0:
            message["zone"] = zone

        channel.basic_publish(
            exchange='rapido-dispatch',
            routing_key=routing_key,
            body=json.dumps(message)
        )

        print(f"Sent: {routing_key} | Order ID: {order_id}", flush=True)

        order_id += 1
        time.sleep(2)

except KeyboardInterrupt:
    print("Dispatcher stopped.")

finally:
    connection.close()
