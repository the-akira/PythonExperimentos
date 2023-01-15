# Flask RabbitMQ

A simple example of how to use **Flask** and **RabbitMQ**.

Start by building and running the application

```
docker-compose up --build
```

To send a message to the queue you must send a request for this route

```
http://localhost:5000/send/hello!
```

To receive a message from the queue you must send a request for this route

```
http://localhost:5000/receive
```

To access the RabbitMQ graphical interface you can follow this URL

```
http://localhost:15672/
```

- **Username:** guest
- **Password:** guest