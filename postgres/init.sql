CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    account_number VARCHAR(50) UNIQUE NOT NULL,
    balance DECIMAL(15,2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO clients (name, account_number, balance) VALUES
('John Doe', 'ACC001', 5000.00),
('Jane Smith', 'ACC002', 7500.50),
('Michael Johnson', 'ACC003', 12000.75),
('Emily Davis', 'ACC004', 3500.25),
('Robert Brown', 'ACC005', 9800.00),
('Sarah Wilson', 'ACC006', 4200.00),
('David Miller', 'ACC007', 15000.00),
('Lisa Anderson', 'ACC008', 6300.50),
('James Taylor', 'ACC009', 8900.75),
('Mary White', 'ACC010', 2500.25);