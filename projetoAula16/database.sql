CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,       -- identificador único do produto
    NomeProduto VARCHAR(100) NOT NULL, -- nome do produto
    Quantidade INT NOT NULL,          -- quantidade disponível
    Preco DECIMAL(10,2) NOT NULL     -- preço do produto
);


INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco)
VALUES 
(1, 'Camiseta', 50, 39.90),
(2, 'Calça Jeans', 30, 79.90),
(3, 'Tênis Esportivo', 20, 199.90);
