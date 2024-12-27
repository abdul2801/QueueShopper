from fastapi import FastAPI
from producer.producer import send_order_event, send_payment_event, send_inventory_event

app = FastAPI()

@app.post("/order")
def create_order(order: dict):
    send_order_event(order)
    return {"status": "Order sent"}

@app.post("/payment")
def process_payment(payment: dict):
    send_payment_event(payment)
    return {"status": "Payment sent"}

@app.post("/inventory")
def update_inventory(inventory: dict):
    send_inventory_event(inventory)
    return {"status": "Inventory update sent"}

from fastapi import WebSocket
from websocket.ws_manager import ws_manager
from consumer.consumer import cursor, conn

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except Exception:
        ws_manager.disconnect(websocket)

def notify_clients(topic, data):
    message = {"topic": topic, "data": data}
    import asyncio
    asyncio.run(ws_manager.broadcast(message))

def process_kafka_event(data, topic):
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
    notify_clients(topic, data)
