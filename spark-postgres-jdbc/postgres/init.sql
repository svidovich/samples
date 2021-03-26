-- You can modify this file to your liking! Add any tables you wish
-- for the database to have.

CREATE USER spark;
CREATE DATABASE spark_test;
GRANT ALL PRIVILEGES ON DATABASE spark_test TO spark;
ALTER USER spark WITH PASSWORD 'test'; -- Beware: you probably shouldn't do this.

\c spark_test

CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL,
    nick_name VARCHAR(64),
    age INTEGER,
    occupation VARCHAR(64)
);

ALTER TABLE test_table OWNER to spark;

INSERT INTO test_table (first_name, last_name, nick_name, age, occupation)
VALUES ('Jeff', 'Lebowski', '"The Dude"', 40, 'Slacker');

INSERT INTO test_table (first_name, last_name, nick_name, age, occupation)
VALUES ('Hank', 'Hill', NULL, 45, 'Assistant Manager');
