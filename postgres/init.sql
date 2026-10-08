CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

INSERT INTO usuarios (name, email) VALUES
    ('Antonio', 'antonio@example.com'),
    ('Maria', 'maria@example.com'),
    ('Juan', 'juan@example.com');