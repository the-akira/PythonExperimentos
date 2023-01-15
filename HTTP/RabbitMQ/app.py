from pika import BlockingConnection, ConnectionParameters
from flask import Flask, jsonify

app = Flask(__name__)

def send_message(message):
    connection = BlockingConnection(ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f'Sent message: {message}')
    connection.close()

def receive_message():
    connection = BlockingConnection(ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    method_frame, header_frame, body = channel.basic_get(queue='hello')
    if method_frame:
        print(f'Received message: {body.decode()}')
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print('No message returned')

    connection.close()
    return body.decode() if body else ''

@app.route('/')
def home():
    api = {
        "Name": "Flask App RabbitMQ Example",
        "Creator": "ChatGPT"
    }
    return jsonify(api)

@app.route('/send/<message>')
def send(message):
    send_message(message)
    return jsonify(message=message)

@app.route('/receive')
def receive():
    message = receive_message()
    return jsonify(message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')