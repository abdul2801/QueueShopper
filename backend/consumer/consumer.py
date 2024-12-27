from kafka import KafkaConsumer
import psycopg2
import json

consumer = KafkaConsumer(
    'order_placed',
    'payment_success',
    'inventory_updated',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

conn = psycopg2.connect(
    dbname="analytics_db",
    user="admin",
    password="password",
    host="postgres"
)

cursor = conn.cursor()

for message in consumer:
    data = message.value
    topic = message.topic

    if topic == 'order_placed':
        cursor.execute("INSERT INTO orders (order_id, user_id, product_id, amount) VALUES (%s, %s, %s, %s)",
                       (data['order_id'], data['user_id'], data['product_id'], data['amount']))

    elif topic == 'payment_success':
        cursor.execute("INSERT INTO payments (payment_id, order_id, status) VALUES (%s, %s, %s)",
                       (data['payment_id'], data['order_id'], data['status']))

    elif topic == 'inventory_updated':
        cursor.execute("UPDATE inventory SET stock = %s WHERE product_id = %s",
                       (data['stock'], data['product_id']))

    conn.commit()
