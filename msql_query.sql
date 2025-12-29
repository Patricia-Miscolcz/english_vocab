create database if not exists english_words;
use english_words;

CREATE TABLE IF NOT EXISTS words (
    id INT AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(100) NOT NULL,
    meaning VARCHAR(255) NOT NULL,
    example TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO words (word, meaning, example) VALUES 
('Apple', 'Maçã', 'I eat an apple every day.');

delete from words where id = 5;
select *from words