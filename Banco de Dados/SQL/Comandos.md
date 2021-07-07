# Comando SQL

## Verificando Tabelas

- `sqlite3 sqlite.db`

- `.tables`

## Ativando Header e Colunas

- `.header on`

- `.mode column`

## Selecionando Dados das Tabelas

- `SELECT * from authors;`

- `SELECT * from books;`

- `SELECT * from books WHERE id = 1;`

- `SELECT * from books WHERE id in (1,2,3);`

- `SELECT * from books WHERE id BETWEEN 1 AND 3;`

- `SELECT * from books WHERE title LIKE 'The D%';`

- `SELECT * FROM books ORDER BY title;`

- `SELECT * FROM books WHERE id >= 3;`