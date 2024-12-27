from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_order_event(order):
    producer.send('order_placed', order)

def send_payment_event(payment):
    producer.send('payment_success', payment)

def send_inventory_event(inventory):
    producer.send('inventory_updated', inventory)
