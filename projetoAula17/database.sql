CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY,          
    ProdutoID INT NOT NULL,              
    FornecedorID INT NOT NULL,          
    Quantidade INT NOT NULL,              
    DataEntrada DATE NOT NULL,            

    CONSTRAINT fk_produto FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    CONSTRAINT fk_fornecedor FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);


SELECT 
    p.NomeProduto,
    f.NomeFornecedor,
    e.Quantidade,
    e.DataEntrada
FROM Produtos p
FULL OUTER JOIN Estoque e ON p.ProdutoID = e.ProdutoID
FULL OUTER JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID;


SELECT 
    f.NomeFornecedor,
    SUM(e.Quantidade) AS TotalRecebido
FROM Estoque e
INNER JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID
GROUP BY f.NomeFornecedor;


ALTER TABLE Estoque
ADD COLUMN PrecoUnitario DECIMAL(10,2);
