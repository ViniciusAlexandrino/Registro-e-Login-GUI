-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS user_auth;
USE user_auth;

-- Criação da tabela de usuários
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
