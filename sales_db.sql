-- Crear base de datos de ventas
CREATE DATABASE SalesDB;

-- Usar base de datos
USE SalesDB;

-- Crear tabla de ventas
CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    Date DATE,
    Salesperson VARCHAR(50),
    Client VARCHAR(50),
    RevenueUSD FLOAT,
    Platform VARCHAR(50)
);
