CREATE TABLE Hospedes
(
    Id int Not Null PRIMARY KEY,
    Numero int,
    Telefone int,
    Cidade varchar(50),
    Estado char(2);
    Id_cliente int Not Null
        Constraint Clientes_Endereços
            FOREIGN KEY (Id_cliente) references Clientes (Id)
)