CREATE TABLE IF NOT EXISTS data(
    id SERIAL PRIMARY KEY,
    my_text text NOT NULL
);

INSERT INTO data (my_text) VALUES
('t0'),
('t1'),
('t1');