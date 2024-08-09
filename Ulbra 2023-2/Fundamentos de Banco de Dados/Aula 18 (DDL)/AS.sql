//*1*//
CREATE TABLE Categoria
(
    Codigo int Not Null PRIMARY KEY,
    Nome varchar(100)
)

CREATE TABLE Produtos
(
    Codigo int Not Null PRIMARY KEY
    Descricao varchar(100),
    Data_Cadastro date,
    Valor_Unit decimal
    Cat_cod int Not Null
        Constraint Categoria
            FOREIGN KEY (Cat_cod) references Categorias(Codigo)
)

CREATE TABLE Pedidos
(
    Cod_Ped int Not Null PRIMARY KEY,
    Total decimal,
    Data_Ped date,
    Cat_cod int Not Null,
        Constraint Categorias
            FOREIGN KEY (Cat_cod) references Categorias(Codigo),
    For_id int Not Null
        Constraint Fornecedores
            FOREIGN KEY (For_id) references Fornecedores(ID)
)

CREATE TABLE Fornecedores
(
    Id int Not Null PRIMARY KEY,
    Nome varchar(100)
)

//*2*//
ALTER TABLE Categorias
Change Column Nome nome_categoria char(50);

//*3*//
SELECT Descricao, Valor_Unit
FROM Produtos
WHERE Codigo = 300;

//*4*//
UPDATE Pedidos
SET Total = 83
WHERE Cod_pede 75;

//*5*//
SELECT *
FROM Pedidos
WHERE Month (Data_pede) = 10;

//*6*//
SELECT *
FROM Produtos
ORDER BY Descricao ASC;