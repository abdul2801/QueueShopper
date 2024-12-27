from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/publish', methods=['POST'])
def publish():
    data = request.json
    topic = data.get('topic')
    message = data.get('message')
    if not topic or not message:
        return jsonify({'error': 'Missing topic or message'}), 400
    producer.send(topic, value=message)
    return jsonify({'status': 'Message sent successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
