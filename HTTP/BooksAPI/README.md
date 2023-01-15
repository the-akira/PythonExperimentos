# Books API

A simple Books API developed with assistance from [ChatGPT](https://chat.openai.com/chat).

## Setting Up

First you must create an `.env` file with the following configurations:

```
POSTGRES_USER=test
POSTGRES_PASSWORD=test
POSTGRES_DB=db
DATABASE_URL=postgresql://test:test@db:5432/db
TESTING=False
```

Start by building and running the application

```
docker-compose up --build
```

Once the application is running, we must initialize the database

```
docker exec -it bookapi_web_1 /bin/bash
```

Inside the container we will access the **Python** interpreter

```
python
```

And then create the database

```python
>>> from app import db
>>> db.create_all()
```

## Testing

To run the tests you must change the TESTING field of the `.env` file to **True**.

```
python tests.py
```

## Loading Data

To load the experimental data you must execute the following **scripts**

```
python load_authors.py
python load_books.py
```